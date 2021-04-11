from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
import re
import time
import asyncio
import logging
import signal
from pyrogram.file_id import FileId
from ..utils.progress_for_pyro import progress_for_pyrogram
from ..translations.trans import Trans
from ..maneuvers.ExecutorManager import ExecutorManager

renamelog = logging.getLogger(__name__)


def add_handlers(client: Client) -> None:
    """This function is responsible to manually register all the bot handlers.

    Args:
        client (pyrogram.Client): Initialized pyrogram client.
    """

    client.add_handler(MessageHandler(start_handler, filters.regex("/start", re.IGNORECASE)))
    client.add_handler(MessageHandler(rename_handler, filters.regex("/rename", re.IGNORECASE)))

    print("added")
    signal.signal(signal.SIGINT, term_handler)
    signal.signal(signal.SIGTERM, term_handler)

async def start_handler(client: Client, msg: Message) -> None:
    await msg.reply(Trans.START_MSG, quote=True)


async def rename_handler(client: Client, msg: Message) -> None:
    rep_msg = msg.reply_to_message
    new_name = msg.text.split(" ",1)[1]
    

    if rep_msg is None:
        await msg.reply("Reply rename to media file.")
        return
    elif not rep_msg.media:
        await msg.reply("Reply rename to media file.")
        return

    msg.download
    queue = asyncio.Queue()

    loop = asyncio.get_event_loop()
    renamelog.debug("Submit the download task")
    loop.create_task(download_fun(client, rep_msg, queue))
    renamelog.debug("Submit the load chunks task")
    loop.create_task(load_chunk_fun(client, rep_msg, queue, new_name))


async def download_fun(client: Client, msg: Message, queue: asyncio.Queue):
    renamelog.debug("start the download")
    try:
        await client.Q_file(FileId.decode(msg.document.file_id), msg.document.file_size, None, queue)
    except:
        renamelog.exception("Error in download_fun")
        await queue.put(False)

async def load_chunk_fun(client,msg: Message,queue: asyncio.Queue, new_file_name: str):
    renamelog.debug("file size "+ str(msg.document.file_size))
    #try:
    #    res = await client.save_file1(queue, msg.document.file_size, msg.document.file_name)
    #except Exception as e:
    #    print(e)
    #print(type(res))
    #rmsg = await msg.reply_document("test.py")
    #await rmsg.edit_media(media=res)
    
    if msg.document.file_size > 10485760:
        progress = await msg.reply("Renaming the file currently hold on.",quote=True)
        try:
            await client.send_document_ipfile(msg.chat.id,queue,msg.document.file_size, new_file_name, progress=progress_for_pyrogram, progress_args=(
                f"Uploading {new_file_name}",
                progress,
                time.time(),
                5,
                client
                ))
        except:
            renamelog.exception("In load chunk fun")
            await progress.edit_text("The download was errored. Report this error.")
    else:
        temp = await msg.reply("Renaming the file currently hold on.",quote=True)
        try:
            await client.send_document_ipfile(msg.chat.id,queue,msg.document.file_size, new_file_name)
        except:
            renamelog.exception("In load chunk fun")
            await temp.edit_text("The download was errored. Report this error.")

def term_handler(signum, frame):
    print("yolo")
    ExecutorManager().stop()