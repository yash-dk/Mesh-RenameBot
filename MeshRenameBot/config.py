from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DB_URI = [str, ""]
