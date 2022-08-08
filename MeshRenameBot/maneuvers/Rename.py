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
from ..core.thumb_manage import get_thumbnail
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# Diff File

renamelog = logging.getLogger(__name__)


class RenameManeuver(DefaultManeuver):
    def __init__(self, client: Client, media_message: Message, cmd_message: Message) -> None:
        super().__init__(client, media_message, cmd_message)
        self._unique_id = int(str(cmd_message.chat.id) + str(cmd_message.id))
        self._fltr_obj = FilterUtils(cmd_message.from_user.id)

    async def execute(self) -> None:
        self._execute_pending = False

        if self._media_message is None:
            await self._cmd_message.reply_text(Trans.REPLY_TO_MEDIA, quote=True)
            return
        elif not self._media_message.media:
            await self._cmd_message.reply_text(Trans.REPLY_TO_MEDIA, quote=True)
            return
        
        self._media_message.from_user = self._cmd_message.from_user

        is_video = False
        is_audio = False

        mime = ""
        try:
            mime = self._media_message.document.mime_type.split("/")[0]
        except:
            pass

        if self._media_message.video is not None:
            is_video = True
        elif self._media_message.audio is not None or self._media_message.voice is not None:
            is_audio = True
        elif mime == "video":
            is_video = True
        elif mime == "audio":
            is_audio = True

        try:
            new_file_name = self._cmd_message.text.split(" ", 1)[1]
        except Exception as e:
            print(e)
            if self._fltr_obj.has_filters():
                
                if self._media_message.document is not None:
                    original_file_name = self._media_message.document.file_name
                elif self._media_message.video is not None:
                    original_file_name = self._media_message.video.file_name
                elif self._media_message.audio is not None or self._media_message.voice is not None:
                    original_file_name = self._media_message.audio.file_name
                else:
                    original_file_name = "no_name"
                
                new_file_name = await self._fltr_obj.filtered_name(original_file_name)
                if original_file_name == new_file_name:
                    await self._cmd_message.reply_text(Trans.RENAME_NO_FILTER_MATCH)
                    return

                await self._cmd_message.reply_text(Trans.RENAME_FILTER_MATCH_USED + f"\nFile name:- {new_file_name}")
            else:
                await self._cmd_message.reply_text(Trans.RENAME_NOFLTR_NONAME)
                return

        markup = InlineKeyboardMarkup([[InlineKeyboardButton(Trans.RENAME_CANCEL,
                                                             "cancel {}".format(self._unique_id))]])

            
        track_msg = f'Execution Started for Rename Task `{self._unique_id}`\n\nUsername: @{self._cmd_message.from_user.username}\n\nName: {self._cmd_message.from_user.mention(style="md")}\n\n'
        track_msg += f'UserID: `{self._cmd_message.from_user.id}`\n\nNew File Name: {new_file_name}'
        await self._client.send_track(track_msg)

        try:
            progress = await self._media_message.reply(Trans.DL_RENAMING_FILE, quote=True, reply_markup=markup)
            dl_path = os.path.join("downloads/{}/".format(str(time.time()).replace(".","")))
            os.makedirs(dl_path, exist_ok=True)
            dl_path = await self._media_message.download(
                file_name=dl_path,
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
            renamelog.info(f"Download Canceled.")
            await progress.edit_text("Download Canceled.")
            return
        
        renamelog.info(f"Download complete to {dl_path}")
        await asyncio.sleep(1)

        
        renamelog.debug("file size " + str(os.path.getsize(dl_path)))
        udb = UserDB()

        
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
        
        try:
            thumb_path = await get_thumbnail(dl_path, self._cmd_message.from_user.id, is_force)
        except:
            renamelog.exception("Thumb error")
            thumb_path = None
        
        renamelog.info(thumb_path)
        renamelog.info(f"is force = {is_force}")
        await progress.edit_text("Downloading Done Now renaming.", reply_markup=None)        

        try:
            ndl_path = os.path.join(os.path.dirname(dl_path), new_file_name)
            os.rename(dl_path,ndl_path)
            
            
            renamelog.info(f"Is force {is_force} is audio {is_audio} is video {is_video}")
            
            new_file_name="**"+new_file_name+"**"  # Bold caption
            
            if is_audio and not is_force:
                try:
                    metadata = extractMetadata(createParser(ndl_path))
                    
                    perfo = ""

                    if self._media_message.audio is not None:
                        duration = self._media_message.audio.duration
                    else:
                        duration = 0
                    
                    if duration == 0:
                        if metadata.has("duration"):
                            duration = metadata.get('duration').seconds
                    
                    if metadata.has("author"):
                        perfo = metadata.get('author')
                except:
                    duration = 0
                    perfo = ""
                
                rmsg = await self._client.send_audio(
                    self._cmd_message.chat.id,
                    ndl_path,
                    duration=duration,
                    performer=perfo,
                    thumb=thumb_path,
                    caption=new_file_name,
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
            
            elif is_video and not is_force:
                try:
                    metadata = extractMetadata(createParser(thumb_path))
                    if metadata.has("width"):
                        width = metadata.get("width")
                    if metadata.has("height"):
                        height = metadata.get("height")
                    
                    metadata = extractMetadata(createParser(ndl_path))
                    if self._media_message.video is not None:
                        duration = self._media_message.video.duration
                    else:
                        duration = 0
                    
                    if duration == 0:
                        if metadata.has("duration"):
                            duration = metadata.get('duration').seconds
                except:
                    renamelog.exception("in here")
                    width = 0
                    height = 0
                    duration = 0

                rmsg = await self._client.send_video(
                    self._cmd_message.chat.id,
                    ndl_path,
                    duration=duration,
                    width=width,
                    height=height,
                    thumb=thumb_path,
                    caption=new_file_name,
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
            
            else:
                rmsg = await self._client.send_document(
                    self._cmd_message.chat.id,
                    ndl_path,
                    thumb=thumb_path,
                    caption=new_file_name,
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
            
            await asyncio.sleep(2) 
        except:
            renamelog.exception("Errored while uplading the file.")
            await progress.edit_text("Rename process errored.")
            return

        rem_this(thumb_path)
        rem_this(ndl_path)
        rem_this(dl_path)
        
        

def rem_this(path):
    try:
        os.remove(path)
    except:
        print(path)
        renamelog.exception("Errored while removeing the file.")
