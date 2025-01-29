from pyrogram import Client, types
from ..database.user_db import UserDB
from .user_input import userin
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import time
from ..translations.trans import Trans
from MeshRenameBot.translations import trans
from typing import Union


class FilterUtils:
    # Filter Types
    REPLACE_FILTER = 1
    REMOVE_FILTER = 2
    ADDITION_FILTER = 3

    # Places
    ADDITION_FILTER_LEFT = 21
    ADDITION_FILTER_RIGHT = 22

    def __init__(self, user_id: int) -> None:
        self._user_db = UserDB()
        self._user_id = user_id
 
    def add_filer(self, ftype: int, first_param: str, second_param: str = None) -> None:
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
                
                if data is None:
                    jdata = {}
                    jdata[str(time.time()).replace(".", "")] = [ftype, first_param]
                else:
                    jdata = json.loads(data)
                    jdata[str(time.time()).replace(".", "")] = [ftype, first_param]
                
                self._user_db.set_var("filters", json.dumps(jdata), user_id)
        elif ftype == self.ADDITION_FILTER:
            if first_param is not None and second_param is not None:
                data = self._user_db.get_var("filters", user_id)
                
                if data is None:
                    jdata = {}
                    jdata[str(time.time()).replace(".", "")] = [ftype, first_param, second_param]
                else:
                    jdata = json.loads(data)
                    jdata[str(time.time()).replace(".", "")] = [ftype, first_param, second_param]
                
                self._user_db.set_var("filters", json.dumps(jdata), user_id)

    def remove_filter(self, filter_id: int) -> None:
        user_id = self._user_id
        if filter_id is not None and user_id is not None:
            data = self._user_db.get_var("filters", user_id)
            
            jdata = json.loads(data)
            jdata.pop(filter_id)
            self._user_db.set_var("filters", json.dumps(jdata), user_id)

    def get_filters(self) -> dict:
        user_id = self._user_id
        
        if user_id is not None:
            data = self._user_db.get_var("filters", user_id)
        
            if data is not None:
                jdata = json.loads(data)
                return jdata
            else:
                return {}

    def get_type_str(self, filt: list) -> str:
        const_str = ""
        if filt[0] == self.ADDITION_FILTER:
            if filt[2] == self.ADDITION_FILTER_LEFT:
                const_str = Trans.FLTR_ADD_LEFT_STR.format(filt[1])

            if filt[2] == self.ADDITION_FILTER_RIGHT:
                const_str = Trans.FLTR_ADD_RIGHT_STR.format(filt[1])

        if filt[0] == self.REMOVE_FILTER:
            const_str = Trans.FLTR_RM_STR.format(filt[1])

        if filt[0] == self.REPLACE_FILTER:
            const_str = Trans.FLTR_REPLACE_STR.format(filt[1], filt[2])
    
        return const_str

    def has_filters(self) -> bool:
        return True if len(self.get_filters()) > 0 else False

    async def filtered_name(self, original_name: str) -> str:
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
            original_name = original_name.replace(i[1], "")
            
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


async def filter_controller(client: Client, msg: types.MessageEntity, is_edit: bool = False) -> None:
    user_id = msg.from_user.id
    fsu = FilterUtils(user_id)
    ufilters = fsu.get_filters()
    fstr = Trans.CURRENT_FLTRS + " \n"

    for i in ufilters.keys():
        fstr += fsu.get_type_str(ufilters[i])
        fstr += "\n"

    rmark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(Trans.ADD_FLTR, "fltr add")],
            [InlineKeyboardButton(Trans.RM_FLTR, "fltr remove")]
        ]
    )
    if is_edit:
        await msg.message.edit_text(fstr, reply_markup=rmark)
    else:
        await msg.reply_text(fstr, quote=True, reply_markup=rmark)

fltr_add = Trans.FILTERS_INTRO


async def filter_interact(client, msg: types.MessageEntity) -> None:
    # fltr type
    data = msg.data.split(" ")
    
    markup1 = InlineKeyboardMarkup(
        [[InlineKeyboardButton(Trans.ADD_REPLACE_FLTR, "fltr addf replace")],
         [InlineKeyboardButton(Trans.ADD_ADDITION_FLTR, "fltr addf addition")],
         [InlineKeyboardButton(Trans.ADD_REMOVE_FLTR, "fltr addf remove")],
         [InlineKeyboardButton(Trans.BACK, "fltr back home")]],
    )

    if data[1] == "add":
        await msg.answer()
        
        await msg.message.edit_text(fltr_add, reply_markup=markup1)
    
    elif data[1] == "remove":
        fsu = FilterUtils(msg.from_user.id)
        if len(data) == 3:
            fsu.remove_filter(data[2])

        ufilters = fsu.get_filters()
        
        fstr = Trans.CURRENT_FLTRS + " \n"
        j = 1
        
        ilinekeys = []
        currline = []
        for i in ufilters.keys():
            fstr += str(j) + ". "
            fstr += fsu.get_type_str(ufilters[i])
            fstr += "\n"
            currline.append(InlineKeyboardButton(str(j), f"fltr remove {i}"))
            j += 1

            if len(currline) == 3:
                ilinekeys.append(currline)
                currline = []
        
        if not currline == []:
            ilinekeys.append(currline)
        
        ilinekeys.append([InlineKeyboardButton(Trans.BACK, "fltr back home")])

        if ilinekeys == []:
            ilinekeys = None
        else:
            ilinekeys = InlineKeyboardMarkup(ilinekeys)

        await msg.message.edit_text(fstr, reply_markup=ilinekeys)
    
    elif data[1] == "addf":
        
        fsu = FilterUtils(msg.from_user.id)

        if data[2] == "replace":
            # Replace Filter Logic

            fltm = Trans.REPALCE_FILTER_INIT_MSG
            await msg.message.edit_text(fltm, reply_markup=None)
            
            inob = userin(client)
            valg = await inob.get_value(client, msg, del_msg=True)
            
            if valg is None:
                await msg.message.edit_text(fltr_add + "\n\n" + Trans.NO_INPUT_FROM_USER, reply_markup=markup1)
            
            elif valg == "ignore":
                await msg.message.edit_text(fltr_add + "\n\n" + Trans.INPUT_IGNORE, reply_markup=markup1)
            
            else:
                if "|" not in valg:
                    await msg.message.edit_text(fltr_add + "\n\n" + Trans.WRONG_INPUT_FORMAT, reply_markup=markup1)
            
                else:
                    valg = valg.split("|", 2)
                    success_add = "\n" + Trans.REPLACE_FILTER_SUCCESS.format(valg[0], valg[1])

                    fsu.add_filer(FilterUtils.REPLACE_FILTER, valg[0], valg[1])
                    
                    await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)

        if data[2] == "addition":
            if len(data) == 4:
                
                inob = userin(client)
                await msg.message.edit_text(Trans.ADDITION_FILTER_INIT_MSG, reply_markup=None)
                valg = await inob.get_value(client, msg, del_msg=True)
                if valg is None:
                    await msg.message.edit_text(fltr_add + "\n\n" + Trans.NO_INPUT_FROM_USER, reply_markup=markup1)
                
                elif valg == "ignore":
                    await msg.message.edit_text(fltr_add + "\n\n" + Trans.INPUT_IGNORE, reply_markup=markup1)

                else:
                    if data[3] == "left":
                        success_add = "\n" + Trans.ADDITION_FILTER_SUCCESS_LEFT.format(valg)
                        fsu.add_filer(FilterUtils.ADDITION_FILTER, valg, FilterUtils.ADDITION_FILTER_LEFT)
                        await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)
                    else:
                        success_add = "\n" + Trans.ADDITION_FILTER_SUCCESS_RIGHT.format(valg)

                        fsu.add_filer(FilterUtils.ADDITION_FILTER, valg, FilterUtils.ADDITION_FILTER_RIGHT)
                        await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)

            else:
                addition_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(Trans.ADDITION_LEFT, "fltr addf addition left")],
                     [InlineKeyboardButton(Trans.ADDITION_RIGHT, "fltr addf addition right")],
                     [InlineKeyboardButton(Trans.BACK, "fltr add")]],
                )
                await msg.message.edit_text(Trans.ADDITION_POSITION_PROMPT, reply_markup=addition_markup)
        
        if data[2] == "remove":
            inob = userin(client)

            await msg.message.edit_text(Trans.REMOVE_FILTER_INIT_MSG, reply_markup=None)
            valg = await inob.get_value(client, msg, del_msg=True)
            if valg is None:
                await msg.message.edit_text(fltr_add + "\n\n" + Trans.NO_INPUT_FROM_USER, reply_markup=markup1)
            
            elif valg == "ignore":
                await msg.message.edit_text(fltr_add + "\n\n" + Trans.INPUT_IGNORE, reply_markup=markup1)

            else:
                success_add = "\n" + Trans.REMOVE_FILTER_SUCCESS.format(valg)
                fsu.add_filer(FilterUtils.REMOVE_FILTER, valg)
                await msg.message.edit_text(fltr_add + success_add, reply_markup=markup1)
    
    elif data[1] == "back":
        if data[2] == "home":
            await filter_controller(client, msg, True)
