from typing import Union
from pyrogram.types.user_and_chats import user

from pyrogram.types.user_and_chats.user import User
from ..database.user_db import UserDB
from PIL import Image
import os
import asyncio
import logging
import time
import random
from ..database.user_db import UserDB
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

#TODO trans pending

renamelog = logging.getLogger(__name__)

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


async def gen_ss(filepath, ts, opfilepath=None):
    # todo check the error pipe and do processing 
    source = filepath
    destination = os.path.dirname(source)
    ss_name =  str(os.path.basename(source)) + "_" + str(round(time.time())) + ".jpg"
    ss_path = os.path.join(destination,ss_name)

    cmd = ["ffmpeg","-loglevel","error","-ss",str(ts),"-i",str(source),"-vframes","1","-q:v","2",str(ss_path)]

    subpr = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    spipe, epipe = await subpr.communicate()
    epipe = epipe.decode().strip()
    spipe = spipe.decode().strip()
    renamelog.info("Stdout Pipe :- {}".format(spipe))
    renamelog.info("Error Pipe :- {}".format(epipe))

    return ss_path

async def resize_img(path,width=None,height=None):
    img = Image.open(path)
    wei,hei = img.size

    wei = width if width is not None else wei
    hei = height if height is not None else hei

    img.thumbnail((wei,hei))
    
    img.save(path,"JPEG")
    return path


async def get_thumbnail(file_path, user_id = None, force_docs = False):
    print(file_path, "-", user_id, "-", force_docs)
    metadata = extractMetadata(createParser(file_path))
    try:
        duration = metadata.get("duration")
    except:
        duration = 3

    if user_id is not None:
        user_thumb = UserDB().get_thumbnail(user_id)
        if force_docs:
            if user_thumb is not False:
                return user_thumb
            else:
                return None
        else:
            if user_thumb is not False:
                return user_thumb
            else:
                path = await gen_ss(file_path,random.randint(2,duration.seconds))
                path = await resize_img(path,320)
                return path

    else:
        if force_docs:
            return None
        
        path = await gen_ss(file_path,random.randint(2,duration.seconds))
        path = await resize_img(path,320)
        return path

async def handle_clr_thumb(client, msg):
    UserDB().set_thumbnail(None, msg.from_user.id)
    await msg.reply_text("Thumbnail Cleared.", quote=True)
