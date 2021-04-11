from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DB_URI = [str, ""]
        API_HASH = [str, "abcdedf......"]
        API_ID = [int, 1234567]
        BOT_TOKEN = [str, "bot:token here"]
