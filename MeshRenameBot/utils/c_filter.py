from re import I
from ..database.user_db import UserDB
from .user_input import userin
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import time, re
from pyrogram import filters
from pyrogram.handlers import MessageHandler

class FilterUtils:
    # Filter Types
    REPLACE_FILTER = 1
    REMOVE_FILTER = 2
    ADDITION_FILTER = 3

    # Places
    ADDITION_FILTER_LEFT = 21
    ADDITION_FILTER_RIGHT = 22

    def __init__(self, user_id):
        self._user_db = UserDB()
        self._user_id = user_id

    
    def add_filer(self, ftype, first_param, second_param = None):
        user_id = self._user_id
        if ftype == self.REPLACE_FILTER:
            if first_param is not None and second_param is not None:
                data = self._user_db.get_var("filters", user_id)
                
                jdata = json.loads(data)
                jdata[str(time.time()).replace(".", "")] = [ftype, first_param, second_param]
                
                self._user_db.set_var("filter", json.dumps(jdata), user_id)
        elif ftype == self.REMOVE_FILTER:
            if first_param is not None:
                data = self._user_db.get_var("filters", user_id)
                
                jdata = json.loads(data)
                jdata[str(time.time()).replace(".", "")] = [ftype, first_param]
                
                self._user_db.set_var("filter", json.dumps(jdata), user_id)
        elif ftype == self.ADDITION_FILTER:
            if first_param is not None and second_param is not None:
                data = self._user_db.get_var("filters", user_id)
                
                jdata = json.loads(data)
                jdata[str(time.time()).replace(".", "")] = [ftype, second_param, first_param]
                
                self._user_db.set_var("filter", json.dumps(jdata), user_id)

    
    def remove_filter(self, filter_id, user_id):
        if filter_id is not None and user_id is not None:
            data = self._user_db.get_var("filters", user_id)
            
            jdata = json.loads(data)
            jdata.pop(filter_id)
            self._user_db.set_var("filter", json.dumps(jdata), user_id)

    
    def get_filters(self):
        user_id = self._user_id
        if user_id is not None:
            data = self._user_db.get_var("filters", user_id)
            if data is not None:
                jdata = json.loads(data)
                return jdata
            else:
                return {}

    def get_type_str(self, filt):
        const_str = ""
        if filt[0] == self.ADDITION_FILTER:
            if filt[2] == self.ADDITION_FILTER_LEFT:
                const_str = "Addition Filter: <code>{}</code> <code>To Left</code>".format(filt[1])

            if filt[2] == self.ADDITION_FILTER_RIGHT:
                const_str = "Addition Filter: <code>{}</code> <code>To Right</code>".format(filt[1])

        if filt[0] == self.REMOVE_FILTER:
            const_str = "Remove Filter: <code>{}</code>".format(filt[1])
        if filt[0] == self.REPLACE_FILTER:
            const_str =  "Replace Filter: <code>{}</code> with <code>{}</code>".format(filt[1], filt[2])
    
        return const_str

async def filter_controller(client, msg):
    user_id = msg.from_user.id
    fsu = FilterUtils(user_id)
    ufilters = fsu.get_filters()
    fstr = "Your Current Filters:- \n"
    for i in ufilters.keys():
        fstr += fsu.get_type_str(ufilters[i])
        fstr += "\n"

    rmark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Add Filter.","fltr add")],
            [InlineKeyboardButton("Remove Filter.","fltr remove")]
        ]
    )
    await msg.reply_text(fstr, quote=True, reply_markup=rmark)

fltr_add = """
Welcome to adding filter.
3 Types of filter.

Replace Filter:- This filter will replace a 
given word with the one you sepcified

Addition Filter:- This filter will add given word
at end ot beginning.

Remove Filter:- This filer will remove given word
from the while file name.

"""

async def filter_interact(client, msg):
    # fltr type
    data = msg.data.split(" ")
    if data[1] == "add":
        await msg.answer()
        markup1 = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Add Replace Filter.","fltr addf replace")],
            [InlineKeyboardButton("Add Addition Filter.","fltr addf addition")],
            [InlineKeyboardButton("Add Remove Filter.","fltr addf remove")],
            [InlineKeyboardButton("Back.","back")]],
        )
        await msg.message.edit_text(fltr_add, reply_markup=markup1)
    
    elif data[1] == "remove":
        fsu = FilterUtils(msg.from_user.id)
        ufilters = fsu.get_filters()
        
        fstr = "Your Current Filters:- \n"
        j = 1
        
        ilinekeys = []
        currline = []
        for i in ufilters.keys():
            fstr += str(j)+". "
            fstr += fsu.get_type_str(ufilters[i])
            fstr += "\n"
            j += 1
            currline.append(InlineKeyboardButton(str(j),f"fltr remove {j}"))

            if len(currline) == 3:
                ilinekeys.append(currline)
                currline = []

        if ilinekeys == []:
            ilinekeys = None
        else:
            ilinekeys = InlineKeyboardMarkup(ilinekeys)

        await msg.message.edit_text(fstr, reply_markup=ilinekeys)
    
    elif data[1] == "addf":
        if data[2] == "replace":
            fltm = "Send the msg in this format. <code>what to replace | what to replace with</code>"
            await msg.message.edit_text(fltm,reply_markup=None)
            
            inob = userin(client)
            valg = await inob.get_value(client, msg)
            print(valg)
