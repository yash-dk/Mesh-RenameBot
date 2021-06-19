from logging import Filter
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
                
                if data is None:
                    jdata = {}
                    jdata[str(time.time()).replace(".", "")] = [ftype, first_param, second_param]
                else:
                    jdata = json.loads(data)
                    jdata[str(time.time()).replace(".", "")] = [ftype, first_param, second_param]
                
                self._user_db.set_var("filters", json.dumps(jdata), user_id)
        elif ftype == self.REMOVE_FILTER:
            if first_param is not None:
                data = self._user_db.get_var("filters", user_id)
                
                jdata = json.loads(data)
                jdata[str(time.time()).replace(".", "")] = [ftype, first_param]
                
                self._user_db.set_var("filters", json.dumps(jdata), user_id)
        elif ftype == self.ADDITION_FILTER:
            if first_param is not None and second_param is not None:
                data = self._user_db.get_var("filters", user_id)
                
                jdata = json.loads(data)
                jdata[str(time.time()).replace(".", "")] = [ftype, first_param, second_param]
                
                self._user_db.set_var("filters", json.dumps(jdata), user_id)

    
    def remove_filter(self, filter_id):
        user_id = self._user_id
        if filter_id is not None and user_id is not None:
            data = self._user_db.get_var("filters", user_id)
            
            jdata = json.loads(data)
            jdata.pop(filter_id)
            self._user_db.set_var("filters", json.dumps(jdata), user_id)

    
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

    def has_filters(self):
        return True if len(self.get_filters()) > 0 else False

    async def filtered_name(self, original_name):
        fltrs = self.get_filters()
        add_filters = []
        remove_filters = []
        replace_filters = []

        for i in fltrs.values():
            if i[0] == self.ADDITION_FILTER:
                add_filters.append(i)
            
            if i[0] == self.REPLACE_FILTER:
                replace_filters.append(i)
            
            if i[0] == self.REMOVE_FILTER:
                remove_filters.append(i)
            
        # Remove First
        for i in remove_filters:
            original_name = original_name.replace(i[1],"")
            
        # Replace second
        for i in replace_filters:
            original_name = original_name.replace(i[1], i[2])


        # Addition At the last.
        for i in add_filters:
            if i[2] == self.ADDITION_FILTER_LEFT:
                original_name = i[1] + original_name
                
            if i[2] == self.ADDITION_FILTER_RIGHT:
                original_name += i[1] 

        return original_name

async def filter_controller(client, msg, is_edit=False):
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
    if is_edit:
        await msg.message.edit_text(fstr, reply_markup=rmark)
    else:
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
    
    markup1 = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Add Replace Filter.","fltr addf replace")],
        [InlineKeyboardButton("Add Addition Filter.","fltr addf addition")],
        [InlineKeyboardButton("Add Remove Filter.","fltr addf remove")],
        [InlineKeyboardButton("Back.","fltr back home")]],
    )

    if data[1] == "add":
        await msg.answer()
        
        await msg.message.edit_text(fltr_add, reply_markup=markup1)
    
    elif data[1] == "remove":
        fsu = FilterUtils(msg.from_user.id)
        if len(data) == 3:
            fsu.remove_filter(data[2])

        ufilters = fsu.get_filters()
        
        fstr = "Your Current Filters:- \n"
        j = 1
        
        ilinekeys = []
        currline = []
        for i in ufilters.keys():
            fstr += str(j)+". "
            fstr += fsu.get_type_str(ufilters[i])
            fstr += "\n"
            currline.append(InlineKeyboardButton(str(j),f"fltr remove {i}"))
            j += 1

            if len(currline) == 3:
                ilinekeys.append(currline)
                currline = []
        
        if not currline == []:
            ilinekeys.append(currline)
        
        ilinekeys.append([InlineKeyboardButton("Back.","fltr back home")])

        if ilinekeys == []:
            ilinekeys = None
        else:
            ilinekeys = InlineKeyboardMarkup(ilinekeys)

        await msg.message.edit_text(fstr, reply_markup=ilinekeys)
    
    elif data[1] == "addf":
        
        fsu = FilterUtils(msg.from_user.id)

        if data[2] == "replace":
            # Replace Filter Logic

            fltm = "Send the msg in this format. <code>what to replace | what to replace with</code>"
            await msg.message.edit_text(fltm,reply_markup=None)
            
            inob = userin(client)
            valg = await inob.get_value(client, msg)
            
            if valg is None:
                await msg.message.edit_text(fltr_add+"\n\n No input received from you.", reply_markup=markup1)
            
            elif valg == "ignore":
                await msg.message.edit_text(fltr_add+"\n\n Received ignore from you.", reply_markup=markup1)
            
            else:
                if not "|" in valg:
                    await msg.message.edit_text(fltr_add+"\n\n The input is not valid. Check the format which is given.", reply_markup=markup1)
            
                else:
                    valg = valg.split("|",2)
                    success_add = "\nAdded the Replace filter successfully. <code>{}</code> will be replaced with <code>{}</code>.".format(valg[0], valg[1])
                    fsu.add_filer(FilterUtils.REPLACE_FILTER,valg[0],valg[1])
                    
                    await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)
        if data[2] == "addition":
            if len(data) == 4:
                ...
                
                inob = userin(client)
                await msg.message.edit_text("Enter the text that you want to add.",reply_markup=None)
                valg = await inob.get_value(client, msg)
                if valg is None:
                    await msg.message.edit_text(fltr_add+"\n\n No input received from you.", reply_markup=markup1)
                
                elif valg == "ignore":
                    await msg.message.edit_text(fltr_add+"\n\n Received ignore from you.", reply_markup=markup1)

                else:
                    if data[3] == "left":
                        success_add = "\nAdded the Addition filter successfully. <code>{}</code> will be added to <code>LEFT</code>.".format(valg)
                        fsu.add_filer(FilterUtils.ADDITION_FILTER, valg, FilterUtils.ADDITION_FILTER_LEFT)
                        await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)
                    else:
                        success_add = "\nAdded the Addition filter successfully. <code>{}</code> will be added to <code>RIGHT</code>.".format(valg)
                        fsu.add_filer(FilterUtils.ADDITION_FILTER, valg, FilterUtils.ADDITION_FILTER_RIGHT)
                        await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)

            else:
                addition_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Addition to LEFT.","fltr addf addition left")],
                    [InlineKeyboardButton("Addition to RIGHT.","fltr addf addition right")],
                    [InlineKeyboardButton("Back.","back")]],
                )
                await msg.message.edit_text("Where do you want to add the text.", reply_markup=addition_markup)
        
        if data[2] == "remove":
            inob = userin(client)

            await msg.message.edit_text("Enter the text that you want to remove.",reply_markup=None)
            valg = await inob.get_value(client, msg)
            if valg is None:
                await msg.message.edit_text(fltr_add+"\n\n No input received from you.", reply_markup=markup1)
            
            elif valg == "ignore":
                await msg.message.edit_text(fltr_add+"\n\n Received ignore from you.", reply_markup=markup1)

            else:
                success_add = "\nAdded the Remove filter successfully. <code>{}</code> will be removed.".format(valg)
                fsu.add_filer(FilterUtils.REMOVE_FILTER, valg)
                await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)
    
    elif data[1] == "back":
        if data[2] == "home":
            await filter_controller(client, msg, True)