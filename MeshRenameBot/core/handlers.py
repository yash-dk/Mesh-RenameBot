from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
import re
from ..utils.SaveFile import SaveFile1
import asyncio
from pyrogram.file_id import FileId

from ..translations.trans import Trans


def add_handlers(client: Client) -> None:
    """This function is responsible to manually register all the bot handlers.

    Args:
        client (pyrogram.Client): Initialized pyrogram client.
    """

    client.add_handler(MessageHandler(start_handler, filters.regex("/start", re.IGNORECASE)))
    client.add_handler(MessageHandler(rename_handler, filters.regex("/rename", re.IGNORECASE)))


async def start_handler(client: Client, msg: Message) -> None:
    await msg.reply(Trans.START_MSG, quote=True)


async def rename_handler(client: Client, msg: Message) -> None:
    rep_msg = msg.reply_to_message

    if rep_msg is None:
        await msg.reply("Reply rename to media file.")
        return
    elif not rep_msg.media:
        await msg.reply("Reply rename to media file.")
        return

    byte_queue = asyncio.Queue(maxsize=0)
    msg.download
    await msg.reply("Renaming now")
    queue = asyncio.Queue()

    loop = asyncio.get_event_loop()
    print("Submit the download task")
    loop.create_task(download_fun(client, rep_msg, queue))
    print("Submit the load chunks task")
    loop.create_task(load_chunk_fun(client, rep_msg, queue))


async def download_fun(client: Client, msg: Message, queue: asyncio.Queue):
    print("start the download")
    
    await client.Q_file(FileId.decode(msg.document.file_id), msg.document.file_size, lambda c,t:print(c,t), queue)


async def load_chunk_fun(client,msg: Message,queue: asyncio.Queue):
    print("file size ", msg.document.file_size)
    #try:
    #    res = await client.save_file1(queue, msg.document.file_size, msg.document.file_name)
    #except Exception as e:
    #    print(e)
    #print(type(res))
    #rmsg = await msg.reply_document("test.py")
    #await rmsg.edit_media(media=res)
    await client.send_document_ipfile(msg.chat.id,queue,msg.document.file_size, msg.document.file_name, thumb="testt.jpg")