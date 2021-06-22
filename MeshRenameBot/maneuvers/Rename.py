from MeshRenameBot.database.user_db import UserDB
from pyrogram.types.messages_and_media.message_entity import MessageEntity
from .Default import DefaultManeuver
from pyrogram import Client, StopTransmission
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import logging
import time
import asyncio
import os
from ..utils.progress_for_pyro import progress_for_pyrogram
from ..core.get_config import get_var
from ..maneuvers.ExecutorManager import ExecutorManager
from ..utils.c_filter import FilterUtils
from pyrogram.file_id import FileId
from ..translations.trans import Trans

# Diff File

renamelog = logging.getLogger(__name__)


class RenameManeuver(DefaultManeuver):
    def __init__(self, client: Client, media_message: Message, cmd_message: Message) -> None:
        super().__init__(client, media_message, cmd_message)
        self._unique_id = int(str(cmd_message.chat.id) + str(cmd_message.message_id))
        self._fltr_obj = FilterUtils(cmd_message.from_user.id)

    async def execute(self) -> None:
        self._media_message.from_user = self._cmd_message.from_user

        try:
            new_file_name = self._cmd_message.text.split(" ", 1)[1]
        except Exception as e:
            print(e)
            if self._fltr_obj.has_filters():
                original_file_name = self._media_message.document.file_name
                new_file_name = await self._fltr_obj.filtered_name(original_file_name)
                if original_file_name == new_file_name:
                    await self._cmd_message.reply_text(Trans.RENAME_NO_FILTER_MATCH)
                    return

                await self._cmd_message.reply_text(Trans.RENAME_FILTER_MATCH_USED)
            else:
                await self._cmd_message.reply_text(Trans.RENAME_NOFLTR_NONAME)
                return

        markup = InlineKeyboardMarkup([[InlineKeyboardButton(Trans.RENAME_CANCEL,
                                                             "cancel {}".format(self._unique_id))]])


        try:
            progress = await self._media_message.reply(Trans.DL_RENAMING_FILE, quote=True, reply_markup=markup)
            dl_path = await self._media_message.download(
                progress=progress_for_pyrogram, 
                progress_args=(
                    "Downloading the file",
                    progress,
                    time.time(),
                    get_var("SLEEP_SECS"),
                    self._client,
                    self._unique_id,
                    markup
                )
            
            )
        except:
            renamelog.exception("Errored while downloading the file.")
            await progress.edit_text("Rename process errored.")
            return
        
        if dl_path is None:
            renamelog.info(f"Download Cancled.")
            await progress.edit_text("Download Cancled.")
            return
        
        renamelog.info(f"Download complete to {dl_path}")
        await asyncio.sleep(1)

        
        renamelog.debug("file size " + str(self._media_message.document.file_size))
        udb = UserDB()
        thumb_path = udb.get_thumbnail(self._media_message.from_user.id)
        if thumb_path is False:
            thumb_path = None
        mode_choice = udb.get_mode(self._media_message.from_user.id)
        is_force = False

        if mode_choice == udb.MODE_SAME_AS_SENT:
            if self._media_message.document is not None:
                is_force = True
            else:
                is_force = False
        elif mode_choice == udb.MODE_AS_DOCUMENT:
            is_force = True
        else:
            is_force = False
        renamelog.info(f"is force = {is_force}")
        await progress.edit_text("Downloading Done Now renaming.", reply_markup=None)        

        try:
            ndl_path = os.path.join(os.path.dirname(dl_path), new_file_name)
            os.rename(dl_path,ndl_path)
            
            rmsg = await self._client.send_document(
                self._cmd_message.chat.id,
                ndl_path,
                thumb=thumb_path,
                force_document=is_force,
                progress=progress_for_pyrogram,
                progress_args=(
                    f"Uploading the file {new_file_name}",
                    progress,
                    time.time(),
                    get_var("SLEEP_SECS"),
                    self._client,
                    self._unique_id,
                    markup
                )
            )
            if rmsg is None:
                await progress.edit_text("Upload Cancled by the user.")
            else:
                await progress.edit_text("Rename process Done.")
            rem_this(thumb_path)
            rem_this(dl_path)
            rem_this(ndl_path)
            return
        except:
            rem_this(dl_path)
            rem_this(ndl_path)
            rem_this(thumb_path)
            renamelog.exception("Errored while uplading the file.")
            await progress.edit_text("Rename process errored.")
            return
        
        

def rem_this(path):
    try:
        os.remove(path)
    except:
        renamelog.info("Errored while removeing the file.")