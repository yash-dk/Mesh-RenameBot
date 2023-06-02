from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, ""]
        API_HASH = [str, "764cb1c8d044fd73dfd61e363594d0ed"]
        API_ID = [int, 29357686]
        BOT_TOKEN = [str, "6140930579:AAH0Qb6g82KunV5clBl1HqgnmImBzP6EeXM"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID = [int, @Saitama_OnePunchMan_0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"@saitama_support_Channel"]
        FORCEJOIN_ID = [int, -1001936973188]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"

