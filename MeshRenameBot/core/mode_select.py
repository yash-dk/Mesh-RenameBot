from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media.message_entity import MessageEntity
from pyrogram.types.user_and_chats.user import User
from ..database.user_db import UserDB
from pyrogram import Client
from pyrogram.types import Message

#TODO trans pending

async def upload_mode(client: Client, msg: Message ) -> None:
    user_id = msg.from_user.id
    udb = UserDB()
    modee = udb.get_mode(user_id)
    
    msg_str =""

    if modee == UserDB.MODE_SAME_AS_SENT:
        msg_str += "➡️ "
    
    msg_str += "1. MODE to the same format as it was sent.\n"    
    if modee == UserDB.MODE_AS_DOCUMENT:
        msg_str += "➡️ "
    
    msg_str += "2. MODE Forced Document.\n"
    
    if modee == UserDB.MODE_AS_GMEDIA:
        msg_str += "➡️ "
    
    msg_str += "3. Mode General Media."

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("1","mode set 0"),
                InlineKeyboardButton("2","mode set 1"),
                InlineKeyboardButton("3","mode set 2"),
            ]
        ]
    )

    
    await msg.reply_text(msg_str, quote=True, reply_markup=markup)

async def mode_callback(client, msg: MessageEntity):
    data = msg.data.split(" ")
    smode = int(data[-1])
    udb = UserDB()
    user_id = msg.message.reply_to_message.from_user.id
    
    udb.set_mode(smode, user_id)
    await msg.answer("Mode changes successfully.")

    msg_str =""

    if smode == UserDB.MODE_SAME_AS_SENT:
        msg_str += "➡️ "
    
    msg_str += "1. MODE to the same format as it was sent.\n"    
    if smode == UserDB.MODE_AS_DOCUMENT:
        msg_str += "➡️ "
    
    msg_str += "2. MODE Forced Document.\n"
    
    if smode == UserDB.MODE_AS_GMEDIA:
        msg_str += "➡️ "
    
    msg_str += "3. Mode General Media."

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("1","mode set 0"),
                InlineKeyboardButton("2","mode set 1"),
                InlineKeyboardButton("3","mode set 2"),
            ]
        ]
    )

    try:
        await msg.message.edit_text(msg_str, reply_markup = markup)
    except:
        pass