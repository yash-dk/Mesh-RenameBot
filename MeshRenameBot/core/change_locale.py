from ..translations import Translator, TRANSLATION_MAP
from ..mesh_bot import MeshRenameBot
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from ..database.user_db import UserDB


async def get_locale_keyboard(user_locale) -> InlineKeyboardMarkup:
    keyboard_markup = InlineKeyboardMarkup([])

    for locale in TRANSLATION_MAP:
        keyboard_markup.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    f"{TRANSLATION_MAP[locale].LANGUAGE_NAME} {TRANSLATION_MAP[locale].LANGUAGE_CODE} {'✅' if TRANSLATION_MAP[locale].LANGUAGE_CODE == user_locale else ''}",
                    callback_data=f"set_locale {TRANSLATION_MAP[locale].LANGUAGE_CODE}",
                )
            ]
        )
    keyboard_markup.inline_keyboard.append(
        [
            InlineKeyboardButton(
                Translator(user_locale).get("CLOSE"),
                callback_data="close",
            )
        ]
    )
    return keyboard_markup


async def change_locale(client: MeshRenameBot, message: Message) -> None:
    user_locale = UserDB().get_var("locale", message.from_user.id)
    translator = Translator(user_locale)

    keyboard_markup = await get_locale_keyboard(user_locale)

    user_locale = UserDB().get_var("locale", message.from_user.id)

    await message.reply_text(
        translator.get("CURRENT_LOCALE", user_locale=user_locale),
        reply_markup=keyboard_markup,
        quote=True,
    )


async def set_locale(client: MeshRenameBot, message: CallbackQuery) -> None:
    user_id = message.from_user.id
    locale = message.data.split()[1]
    UserDB().set_var("locale", locale, user_id)
    keyboard_markup = await get_locale_keyboard(locale)

    await message.message.edit_text(
        Translator(locale).get("CURRENT_LOCALE", user_locale=locale),
        reply_markup=keyboard_markup,
    )
