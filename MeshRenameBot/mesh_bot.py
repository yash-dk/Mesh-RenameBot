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
    ...