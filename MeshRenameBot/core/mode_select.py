from pyrogram.types.bots_and_keyboards.inline_keyboard_button import (
    InlineKeyboardButton,
)
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import (
    InlineKeyboardMarkup,
)
from pyrogram.types import CallbackQuery
from pyrogram.types.user_and_chats.user import User
from ..database.user_db import UserDB
from ..mesh_bot import MeshRenameBot
from pyrogram.types import Message
from ..translations import Translator


async def generate_mode_message(user_id):
    udb = UserDB()
    modee = udb.get_mode(user_id)
    command_mode = udb.get_var("command_mode", user_id)
    command_mode = (
        command_mode if command_mode is not None else UserDB.MODE_RENAME_WITH_COMMAND
    )

    user_locale = udb.get_var("locale", user_id)
    translator = Translator(user_locale)

    msg_str = translator.get(
        "MODE_INITIAL_MSG", mode=modee, command_mode=command_mode, udb=UserDB
    )

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(translator.get("MODE_SET_0"), "mode set 0"),
                InlineKeyboardButton(translator.get("MODE_SET_1"), "mode set 1"),
                InlineKeyboardButton(translator.get("MODE_SET_2"), "mode set 2"),
            ],
            [
                InlineKeyboardButton(translator.get("COMMAND_MODE_SET_3"), "command_mode set 3"),
                InlineKeyboardButton(translator.get("COMMAND_MODE_SET_4"), "command_mode set 4"),
            ],
            [
                InlineKeyboardButton(translator.get("CLOSE"), "close"),
            ],
        ]
    )

    return msg_str, markup


async def upload_mode(_: MeshRenameBot, msg: Message) -> None:
    user_id = msg.from_user.id
    msg_str, markup = await generate_mode_message(user_id)
    await msg.reply_text(msg_str, quote=True, reply_markup=markup)


async def mode_callback(_: MeshRenameBot, msg: CallbackQuery):
    data = msg.data.split(" ")
    mode_type = data[0]  # Either 'mode' or 'command_mode'
    mode_value = int(data[-1])

    udb = UserDB()
    user_id = msg.message.reply_to_message.from_user.id

    if mode_type == "mode":
        udb.set_mode(mode_value, user_id)
    elif mode_type == "command_mode":
        udb.set_var("command_mode", mode_value, user_id)

    msg_str, markup = await generate_mode_message(user_id)

    try:
        await msg.message.edit_text(msg_str, reply_markup=markup)
    except:
        pass
