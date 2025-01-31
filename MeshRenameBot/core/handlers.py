from os import rename
from MeshRenameBot.core.get_config import get_var
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
import re
import logging
import signal
import asyncio
from ..maneuvers.ExecutorManager import ExecutorManager
from ..maneuvers.Rename import RenameManeuver
from ..utils.c_filter import filter_controller, filter_interact
from ..utils.user_input import interactive_input
from .thumb_manage import handle_set_thumb, handle_get_thumb, handle_clr_thumb
from .mode_select import upload_mode, mode_callback
from ..config import Commands
from ..translations import Translator, TRANSLATION_MAP
from ..database.user_db import UserDB
from .caption_manage import set_caption, del_caption
from ..mesh_bot import MeshRenameBot
from .change_locale import change_locale, set_locale

renamelog = logging.getLogger(__name__)


def add_handlers(client: MeshRenameBot) -> None:
    """This function is responsible to manually register all the bot handlers.

    Args:
        client (pyrogram.Client): Initialized pyrogram client.
    """

    client.add_handler(MessageHandler(intercept_handler))
    client.add_handler(MessageHandler(interactive_input))
    client.add_handler(
        MessageHandler(start_handler, filters.regex(Commands.START, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(rename_handler, filters.regex(Commands.RENAME, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(
            rename_handler,
            filters.document | filters.video | filters.audio | filters.photo,
        )
    )
    client.add_handler(
        MessageHandler(
            filter_controller, filters.regex(Commands.FILTERS, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(
            handle_set_thumb, filters.regex(Commands.SET_THUMB, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(
            handle_get_thumb, filters.regex(Commands.GET_THUMB, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(
            handle_clr_thumb, filters.regex(Commands.CLR_THUMB, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(handle_queue, filters.regex(Commands.QUEUE, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(upload_mode, filters.regex(Commands.MODE, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(help_str, filters.regex(Commands.HELP, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(set_caption, filters.regex(Commands.SET_CAPTION, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(change_locale, filters.regex(Commands.SET_LANG, re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(cancel_this, filters.regex("cancel", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(filter_interact, filters.regex("fltr", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(mode_callback, filters.regex("mode", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(
            mode_callback, filters.regex("command_mode", re.IGNORECASE)
        )
    )
    client.add_handler(
        CallbackQueryHandler(close_message, filters.regex("close", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(del_caption, filters.regex("delcaption", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(set_locale, filters.regex("set_locale", re.IGNORECASE))
    )

    signal.signal(signal.SIGINT, term_handler)
    signal.signal(signal.SIGTERM, term_handler)


async def start_handler(_: MeshRenameBot, msg: Message) -> None:
    user_locale = UserDB().get_var("locale", msg.from_user.id)

    await msg.reply(Translator(user_locale).get("START_MSG"), quote=True)


async def rename_handler(client: MeshRenameBot, msg: Message) -> None:
    command_mode = UserDB().get_var("command_mode", msg.from_user.id)
    user_locale = UserDB().get_var("locale", msg.from_user.id)
    translator = Translator(user_locale)

    if command_mode == UserDB.MODE_RENAME_WITHOUT_COMMAND:
        if msg.media is None:
            return
        rep_msg = msg
    else:
        if msg.media:
            return
        rep_msg = msg.reply_to_message

    if rep_msg is None:
        await msg.reply_text(translator.get("REPLY_TO_MEDIA"), quote=True)

    file_id = await client.get_file_id(rep_msg)
    if file_id is not None:
        await msg.reply_text(
            translator.get(
                "RENAME_ADDED_TO_QUEUE", dc_id=file_id.dc_id, media_id=file_id.media_id
            ),
            quote=True,
        )

    await client.send_track(
        translator.get(
            "TRACK_MESSAGE_ADDED_RENAME",
            username=msg.from_user.username,
            name=msg.from_user.first_name,
            user_id=msg.from_user.id,
        )
    )
    await asyncio.sleep(2)
    await ExecutorManager().create_maneuver(RenameManeuver(client, rep_msg, msg))


async def help_str(_: MeshRenameBot, msg: Message) -> None:
    user_locale = UserDB().get_var("locale", msg.from_user.id)
    await msg.reply_text(
        Translator(user_locale).get(
            "HELP_STR",
            startcmd=Commands.START,
            renamecmd=Commands.RENAME,
            filterscmd=Commands.FILTERS,
            setthumbcmd=Commands.SET_THUMB,
            getthumbcmd=Commands.GET_THUMB,
            clrthumbcmd=Commands.CLR_THUMB,
            modecmd=Commands.MODE,
            queuecmd=Commands.QUEUE,
            setcaptioncmd=Commands.SET_CAPTION,
            helpcmd=Commands.HELP,
        ),
        quote=True,
    )


def term_handler(signum: int, frame: int) -> None:
    ExecutorManager().stop()


async def cancel_this(_: MeshRenameBot, msg: CallbackQuery) -> None:
    data = str(msg.data).split(" ")
    ExecutorManager().canceled_uids.append(int(data[1]))
    user_locale = UserDB().get_var("locale", msg.from_user.id)
    await msg.answer(Translator(user_locale).get("CANCEL_MESSAGE"), show_alert=True)


async def handle_queue(_: MeshRenameBot, msg: Message) -> None:
    EM = ExecutorManager()
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    j = 0
    for i in EM.all_maneuvers_log:
        if i.is_pending:
            j += 1
    q_len = j

    j = 0
    for i in EM.all_maneuvers_log:
        if i.is_executing:
            j += 1
    currently_exec = j

    from_id = msg.from_user.id
    max_size = get_var("MAX_QUEUE_SIZE")

    fmsg = translator.get(
        "RENAME_QUEUE_STATUS",
        total_tasks=q_len,
        queue_capacity=max_size,
        current_task=currently_exec,
    )

    j = 1
    for i in EM.all_maneuvers_log:
        if i.sender_id == from_id:
            fmsg += translator.get(
                "RENAME_QUEUE_USER_STATUS",
                is_executing=i.is_executing,
                is_pending=i.is_pending,
                task_id=i._unique_id,
                task_number=j,
            )

        if i.is_pending:
            j += 1

    await msg.reply_text(fmsg)


async def intercept_handler(client: Client, msg: Message) -> None:
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    if get_var("FORCEJOIN") != "":
        try:
            user_state = await client.get_chat_member(
                get_var("FORCEJOIN_ID"), msg.from_user.id
            )
            if user_state.status == "kicked":
                await msg.reply_text(translator.get("USER_KICKED"), quote=True)
                return
        except UserNotParticipant:
            forcejoin = get_var("FORCEJOIN")
            await msg.reply_text(
                translator.get("JOIN_CHANNEL"),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                translator.get("JOIN_CHANNEL"), url=f"{forcejoin}"
                            )
                        ]
                    ]
                ),
                parse_mode="markdown",
            )
            return
        except ChatAdminRequired:
            renamelog.error("The bot is not the admin in the chat make it admin first.")
            return
        except UsernameNotOccupied:
            renamelog.error("Invalid FORCEJOIN ID can find that chat.")
            return
        except:
            renamelog.exception(
                "The ID should be of the channel/ group that you want the user to join."
            )
            return

    await msg.continue_propagation()


async def close_message(_: MeshRenameBot, msg: CallbackQuery) -> None:
    if msg.message.reply_to_message is not None:
        await msg.message.reply_to_message.delete()
    await msg.message.delete()
