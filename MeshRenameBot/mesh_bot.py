from pyrogram import Client, raw, utils, StopTransmission, types
from pyrogram.file_id import FileId, FileType, ThumbnailSource
from pyrogram.session import Auth, Session
from pyrogram.errors import (
    SessionPasswordNeeded,
    VolumeLocNotFound, ChannelPrivate,
    AuthBytesInvalid, BadRequest, FilePartMissing
)
from pyrogram.crypto import aes
from hashlib import sha256
from asyncio import Queue
from hashlib import md5
from pathlib import PurePath
from typing import Union, List, Optional

import os
import tempfile
import asyncio
import functools
import inspect
import io
import logging
import math
import os

renamelog = logging.getLogger(__name__)

# Diff File


class MeshRenameBot(Client):
    async def get_file_id(self, message):
        available_media = ("audio", "document", "photo", "sticker", "animation", "video", "voice", "video_note",
                           "new_chat_photo")

        if isinstance(message, types.Message):
            for kind in available_media:
                media = getattr(message, kind, None)

                if media is not None:
                    break
            else:
                raise ValueError("This message doesn't contain any downloadable media")
        else:
            media = message

        if isinstance(media, str):
            file_id_str = media
        else:
            file_id_str = media.file_id

        file_id_obj = FileId.decode(file_id_str)
        
        return file_id_obj