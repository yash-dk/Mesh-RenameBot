from abc import ABC, abstractmethod
import re
from pyrogram import Client, raw
from pyrogram.types import Message


class DefaultManeuver(ABC):
    def __init__(self, client: Client, media_message: Message, cmd_message: Message) -> None:
        self._client = client
        self._media_message = media_message
        self._cmd_message = cmd_message
        self._sender_id = cmd_message.from_user.id
        self._chat_id = cmd_message.chat.id
        self._unique_id = 0

        self._canceled = False  # Track the cancel status
        self._halt = False  # Track if the maneuver is halted [not implemented]
        self._execute_pending = True
        self._done = False
    
    @property
    def sender_id(self) -> int:
        return self._sender_id

    @property
    def chat_id(self) -> int:
        return self._chat_id

    @abstractmethod
    async def execute(self) -> None:
        raise NotImplementedError("Not implemented the method execute from the calling class.")
    
    def cancel(self) -> None:
        self._execute_pending = False
        self._done = True
        self._canceled = True
    
    def halt(self) -> None:
        self._halt = True

    def done(self) -> None:
        self._done = True

    @property
    def is_halted(self) -> bool:
        return self._halt

    @property
    def is_executing(self) -> bool:
        if not self._done and not self._execute_pending:
            return True
        else:
            return False

    @property
    def is_pending(self) -> bool:
        return self._execute_pending

    @property
    def is_canceled(self) -> bool:
        return self._canceled

    @property
    def is_done(self) -> bool:
        return self._done