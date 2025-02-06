from pyrogram import Client, types
from pyrogram.file_id import FileId

import logging
from MeshRenameBot.core.get_config import get_var

renamelog = logging.getLogger(__name__)

# Diff File

class MeshRenameBot(Client):
    async def get_file_id(self, message):
        available_media = (
            "audio",
            "document",
            "photo",
            "sticker",
            "animation",
            "video",
            "voice",
            "video_note",
            "new_chat_photo",
        )

        if isinstance(message, types.Message):
            for kind in available_media:
                media = getattr(message, kind, None)

                if media is not None:
                    break
            else:
                return None
        else:
            media = message

        if isinstance(media, str):
            file_id_str = media
        else:
            file_id_str = media.file_id

        file_id_obj = FileId.decode(file_id_str)

        return file_id_obj

    async def send_track(self, text_mess):
        track_channel = get_var("TRACE_CHANNEL")
        if track_channel != 0:
            try:
                await self.send_message(track_channel, text_mess)
            except:
                renamelog.exception(
                    "Make Sure to enter the Track Channel ID correctly."
                )
