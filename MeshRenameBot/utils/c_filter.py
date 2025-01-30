from pyrogram import Client, types
from ..database.user_db import UserDB
from .user_input import userin
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import time
from ..translations import Translator
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
                    jdata[str(time.time()).replace(".", "")] = [
                        ftype,
                        first_param,
                        second_param,
                    ]
                else:
                    jdata = json.loads(data)
                    jdata[str(time.time()).replace(".", "")] = [
                        ftype,
                        first_param,
                        second_param,
                    ]

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
                    jdata[str(time.time()).replace(".", "")] = [
                        ftype,
                        first_param,
                        second_param,
                    ]
                else:
                    jdata = json.loads(data)
                    jdata[str(time.time()).replace(".", "")] = [
                        ftype,
                        first_param,
                        second_param,
                    ]

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

    def get_type_str(self, filt: list, user_locale: str = None) -> str:
        translator = Translator(user_locale)

        const_str = ""
        if filt[0] == self.ADDITION_FILTER:
            if filt[2] == self.ADDITION_FILTER_LEFT:
                const_str = translator.get("FLTR_ADD_LEFT_STR", text_1=filt[1])

            if filt[2] == self.ADDITION_FILTER_RIGHT:
                const_str = translator.get("FLTR_ADD_RIGHT_STR", text_1=filt[1])

        if filt[0] == self.REMOVE_FILTER:
            const_str = translator.get("FLTR_RM_STR", text_1=filt[1])

        if filt[0] == self.REPLACE_FILTER:
            const_str = translator.get(
                "FLTR_REPLACE_STR", text_1=filt[1], text_2=filt[2]
            )

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


async def filter_controller(
    _: Client, msg: Union[types.Message, types.CallbackQuery], is_edit: bool = False
) -> None:
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    fsu = FilterUtils(user_id)
    ufilters = fsu.get_filters()
    fstr = translator.get("CURRENT_FLTRS") + " \n"

    for i in ufilters.keys():
        fstr += fsu.get_type_str(ufilters[i], user_locale)
        fstr += "\n"

    rmark = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(translator.get("ADD_FLTR"), "fltr add")],
            [InlineKeyboardButton(translator.get("RM_FLTR"), "fltr remove")],
            [InlineKeyboardButton("Close", "close")],
        ]
    )
    if is_edit:
        await msg.message.edit_text(fstr, reply_markup=rmark)
    else:
        await msg.reply_text(fstr, quote=True, reply_markup=rmark)


async def filter_interact(client, msg: types.CallbackQuery) -> None:
    # fltr type
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)
    fltr_add = translator.get("FILTERS_INTRO")

    data = msg.data.split(" ")

    markup1 = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    translator.get("ADD_REPLACE_FLTR"), "fltr addf replace"
                )
            ],
            [
                InlineKeyboardButton(
                    translator.get("ADD_ADDITION_FLTR"), "fltr addf addition"
                )
            ],
            [
                InlineKeyboardButton(
                    translator.get("ADD_REMOVE_FLTR"), "fltr addf remove"
                )
            ],
            [InlineKeyboardButton(translator.get("BACK"), "fltr back home")],
        ],
    )

    if data[1] == "add":
        await msg.answer()

        await msg.message.edit_text(fltr_add, reply_markup=markup1)

    elif data[1] == "remove":
        fsu = FilterUtils(msg.from_user.id)
        if len(data) == 3:
            fsu.remove_filter(data[2])

        ufilters = fsu.get_filters()

        fstr = translator.get("CURRENT_FLTRS") + " \n"
        j = 1

        ilinekeys = []
        currline = []
        for i in ufilters.keys():
            fstr += str(j) + ". "
            fstr += fsu.get_type_str(ufilters[i], user_locale)
            fstr += "\n"
            currline.append(InlineKeyboardButton(str(j), f"fltr remove {i}"))
            j += 1

            if len(currline) == 3:
                ilinekeys.append(currline)
                currline = []

        if not currline == []:
            ilinekeys.append(currline)

        ilinekeys.append(
            [InlineKeyboardButton(translator.get("BACK"), "fltr back home")]
        )

        if ilinekeys == []:
            ilinekeys = None
        else:
            ilinekeys = InlineKeyboardMarkup(ilinekeys)

        await msg.message.edit_text(fstr, reply_markup=ilinekeys)

    elif data[1] == "addf":

        fsu = FilterUtils(msg.from_user.id)

        if data[2] == "replace":
            # Replace Filter Logic

            fltm = translator.get("REPALCE_FILTER_INIT_MSG")
            await msg.message.edit_text(fltm, reply_markup=None)

            inob = userin(client)
            valg = await inob.get_value(client, msg, del_msg=True)

            if valg is None:
                await msg.message.edit_text(
                    fltr_add + "\n\n" + translator.get("NO_INPUT_FROM_USER"),
                    reply_markup=markup1,
                )

            elif valg == "ignore":
                await msg.message.edit_text(
                    fltr_add + "\n\n" + translator.get("INPUT_IGNORE"),
                    reply_markup=markup1,
                )

            else:
                if "|" not in valg:
                    await msg.message.edit_text(
                        fltr_add + "\n\n" + translator.get("WRONG_INPUT_FORMAT"),
                        reply_markup=markup1,
                    )

                else:
                    valg = valg.split("|", 2)
                    success_add = "\n" + translator.get(
                        "REPLACE_FILTER_SUCCESS", text_1=valg[0], text_2=valg[1]
                    )

                    fsu.add_filer(FilterUtils.REPLACE_FILTER, valg[0], valg[1])

                    await msg.message.edit_text(
                        fltr_add + success_add, reply_markup=markup1
                    )

        if data[2] == "addition":
            if len(data) == 4:

                inob = userin(client)
                await msg.message.edit_text(
                    translator.get("ADDITION_FILTER_INIT_MSG"), reply_markup=None
                )
                valg = await inob.get_value(client, msg, del_msg=True)
                valg = valg.strip("|")
                if valg is None:
                    await msg.message.edit_text(
                        fltr_add + "\n\n" + translator.get("NO_INPUT_FROM_USER"),
                        reply_markup=markup1,
                    )

                elif valg == "ignore":
                    await msg.message.edit_text(
                        fltr_add + "\n\n" + translator.get("INPUT_IGNORE"),
                        reply_markup=markup1,
                    )

                else:
                    if data[3] == "left":
                        success_add = "\n" + translator.get(
                            "ADDITION_FILTER_SUCCESS_LEFT", text_1=valg
                        )
                        fsu.add_filer(
                            FilterUtils.ADDITION_FILTER,
                            valg,
                            FilterUtils.ADDITION_FILTER_LEFT,
                        )
                        await msg.message.edit_text(
                            fltr_add + success_add, reply_markup=markup1
                        )
                    else:
                        success_add = "\n" + translator.get(
                            "ADDITION_FILTER_SUCCESS_RIGHT", text_1=valg
                        )

                        fsu.add_filer(
                            FilterUtils.ADDITION_FILTER,
                            valg,
                            FilterUtils.ADDITION_FILTER_RIGHT,
                        )
                        await msg.message.edit_text(
                            fltr_add + success_add, reply_markup=markup1
                        )

            else:
                addition_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                translator.get("ADDITION_LEFT"),
                                "fltr addf addition left",
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                translator.get("ADDITION_RIGHT"),
                                "fltr addf addition right",
                            )
                        ],
                        [InlineKeyboardButton(translator.get("BACK"), "fltr add")],
                    ],
                )
                await msg.message.edit_text(
                    translator.get("ADDITION_POSITION_PROMPT"),
                    reply_markup=addition_markup,
                )

        if data[2] == "remove":
            inob = userin(client)

            await msg.message.edit_text(
                translator.get("REMOVE_FILTER_INIT_MSG"), reply_markup=None
            )
            valg = await inob.get_value(client, msg, del_msg=True)
            if valg is None:
                await msg.message.edit_text(
                    fltr_add + "\n\n" + translator.get("NO_INPUT_FROM_USER"),
                    reply_markup=markup1,
                )

            elif valg == "ignore":
                await msg.message.edit_text(
                    fltr_add + "\n\n" + translator.get("INPUT_IGNORE"),
                    reply_markup=markup1,
                )

            else:
                success_add = "\n" + translator.get(
                    "REMOVE_FILTER_SUCCESS", text_1=valg
                )
                fsu.add_filer(FilterUtils.REMOVE_FILTER, valg)
                await msg.message.edit_text(
                    fltr_add + success_add, reply_markup=markup1
                )

    elif data[1] == "back":
        if data[2] == "home":
            await filter_controller(client, msg, True)
