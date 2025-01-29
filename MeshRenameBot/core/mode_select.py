from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media.message_entity import MessageEntity
from pyrogram.types.user_and_chats.user import User
from ..database.user_db import UserDB
from pyrogram import Client
from pyrogram.types import Message

async def generate_mode_message(user_id):
    udb = UserDB()
    modee = udb.get_mode(user_id)
    command_mode = udb.get_var("command_mode", user_id)
    command_mode = command_mode if command_mode is not None else UserDB.MODE_RENAME_WITH_COMMAND

    msg_str = "File output mode: \n\n"

    msg_str += "➡️ " if modee == UserDB.MODE_SAME_AS_SENT else ""
    msg_str += "1. MODE to the same format as it was sent.\n"

    msg_str += "➡️ " if modee == UserDB.MODE_AS_DOCUMENT else ""
    msg_str += "2. MODE Forced Document.\n"

    msg_str += "➡️ " if modee == UserDB.MODE_AS_GMEDIA else ""
    msg_str += "3. Mode General Media.\n"

    msg_str += "\n\nSelect the mode for renaming files:\n"

    msg_str += "➡️ " if command_mode == UserDB.MODE_RENAME_WITH_COMMAND else ""
    msg_str += "A. Rename with command.\n"

    msg_str += "➡️ " if command_mode == UserDB.MODE_RENAME_WITHOUT_COMMAND else ""
    msg_str += "B. Rename without command."

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("1", "mode set 0"),
                InlineKeyboardButton("2", "mode set 1"),
                InlineKeyboardButton("3", "mode set 2"),
            ],
            [
                InlineKeyboardButton("A", "command_mode set 3"),
                InlineKeyboardButton("B", "command_mode set 4"),
            ],
            [
                InlineKeyboardButton("Close", "close"),
            ]
        ]
    )

    return msg_str, markup


async def upload_mode(client: Client, msg: Message) -> None:
    user_id = msg.from_user.id
    msg_str, markup = await generate_mode_message(user_id)
    await msg.reply_text(msg_str, quote=True, reply_markup=markup)


async def mode_callback(client, msg: MessageEntity):
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
