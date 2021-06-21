from ..database.user_db import UserDB
from pyrogram import Client
from pyrogram.types import Message

#TODO trans pending

async def upload_mode(client: Client, msg: Message) -> None:
    user_id = msg.from_user.id
    udb = UserDB()
    modee = udb.get_mode(user_id)
    modee = (modee + 1) % 3
    udb.set_mode(modee, user_id)
    
    msg_str = ""
    
    if modee == UserDB.MODE_SAME_AS_SENT:
        msg_str += "The mode is changed to the same format as it was sent."
    if modee == UserDB.MODE_AS_DOCUMENT:
        msg_str += "The mode is changed to the FORCED DOCUEMENT."
    if modee == UserDB.MODE_AS_GMEDIA:
        msg_str += "The mode is changed to the General Media."

    await msg.reply_text(msg_str, quote=True)