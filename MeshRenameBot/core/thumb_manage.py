from typing import Union
from ..database.user_db import UserDB
from PIL import Image
import os
import asyncio

async def adjust_image(path: str) -> Union[str, None]:
    try:
        im = Image.open(path)
        im.convert("RGB").save(path,"JPEG")
        im = Image.open(path)
        im.thumbnail((320,320), Image.ANTIALIAS)
        im.save(path,"JPEG")
        return path
    except Exception:
        return

async def handle_set_thumb(client, msg):
    original_message = msg.reply_to_message
    if original_message.photo is not None:
        path = await original_message.download()
        path = await adjust_image(path)
        if path is not None:
            with open(path, "rb") as file_handle:
                data = file_handle.read()
                UserDB().set_thumbnail(data, msg.from_user.id)
            
            os.remove(path)
            await msg.reply_text("Thumbnail set success.", quote=True)
        else:
            await msg.reply_text("Reply to an image to set it as a thumbnail.", quote=True)

    else:
        await msg.reply_text("Reply to an image to set it as a thumbnail.", quote=True)

async def handle_get_thumb(client, msg):
    thumb_path = UserDB().get_thumbnail(msg.from_user.id)
    if thumb_path is False:
        await msg.reply("No Thumbnail Found.", quote=True)
    else:
        await msg.reply_photo(thumb_path, quote=True)
        os.remove(thumb_path)


async def handle_clr_thumb(client, msg):
    UserDB().set_thumbnail(None, msg.from_user.id)
    await msg.reply_text("Thumbnail Cleared.", quote=True)
