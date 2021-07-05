from MeshRenameBot.core.get_config import get_var
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import Message
import re
import logging
import signal
import asyncio
from ..translations.trans import Trans
from ..maneuvers.ExecutorManager import ExecutorManager
from ..maneuvers.Rename import RenameManeuver
from ..utils.c_filter import filter_controller, filter_interact
from ..utils.user_input import interactive_input
from .thumb_manage import handle_set_thumb, handle_get_thumb, handle_clr_thumb
from .mode_select import upload_mode, mode_callback

renamelog = logging.getLogger(__name__)


def add_handlers(client: Client) -> None:
    """This function is responsible to manually register all the bot handlers.

    Args:
        client (pyrogram.Client): Initialized pyrogram client.
    """

    client.add_handler(MessageHandler(interactive_input))
    client.add_handler(MessageHandler(start_handler, filters.regex("/start", re.IGNORECASE)))
    client.add_handler(MessageHandler(rename_handler, filters.regex("/rename", re.IGNORECASE)))
    client.add_handler(CallbackQueryHandler(cancel_this, filters.regex("cancel", re.IGNORECASE)))
    client.add_handler(MessageHandler(filter_controller, filters.regex("/filters", re.IGNORECASE)))
    client.add_handler(MessageHandler(handle_set_thumb, filters.regex("/setthumb", re.IGNORECASE)))
    client.add_handler(MessageHandler(handle_get_thumb, filters.regex("/getthumb", re.IGNORECASE)))
    client.add_handler(MessageHandler(handle_clr_thumb, filters.regex("/clrthumb", re.IGNORECASE)))
    client.add_handler(MessageHandler(handle_queue, filters.regex("/queue", re.IGNORECASE)))
    client.add_handler(MessageHandler(upload_mode, filters.regex("/mode", re.IGNORECASE)))
    client.add_handler(CallbackQueryHandler(filter_interact, filters.regex("fltr", re.IGNORECASE)))
    client.add_handler(CallbackQueryHandler(mode_callback, filters.regex("mode", re.IGNORECASE)))

    signal.signal(signal.SIGINT, term_handler)
    signal.signal(signal.SIGTERM, term_handler)


async def start_handler(client: Client, msg: Message) -> None:
    await msg.reply(Trans.START_MSG, quote=True)


async def rename_handler(client: Client, msg: Message) -> None:
    rep_msg = msg.reply_to_message
    file_id = await client.get_file_id(rep_msg)
    if file_id is not None:
        rmsg = f"""Added the Rename to queue.
        DC ID   :- {file_id.dc_id}
        Media ID:- {file_id.media_id}
        """
        await msg.reply_text(rmsg)
    await asyncio.sleep(2)
    await ExecutorManager().create_maneuver(RenameManeuver(client, rep_msg, msg))
    


def term_handler(signum: int, frame: int) -> None:
    ExecutorManager().stop()


async def cancel_this(client: Client, msg: Message) -> None:
    data = str(msg.data).split(" ")
    ExecutorManager().canceled_uids.append(int(data[1]))
    await msg.answer(Trans.CANCEL_MESSAGE, show_alert=True)

async def handle_queue(client: Client, msg: Message) -> None:
    EM = ExecutorManager()

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

    fmsg = f"Total Tasks in Queue:- {q_len}\nCapacity{max_size}\nCurrently Executing{currently_exec}\n\n"

    j = 1
    for i in EM.all_maneuvers_log:
        if i.sender_id == from_id:
            if i.is_executing:
                fmsg += f"Your Task Is Executing\nTask Unique Number {i._unique_id}\n\n"
            if i.is_pending:
                fmsg += f"Your Task Number in Queue: {j}\nTask Unique Number {i._unique_id}\n\n"
        
        if i.is_pending:
            j += 1

    await msg.reply_text(fmsg)