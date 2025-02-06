from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from ..database.user_db import UserDB
from ..translations import Translator


def get_inline_keyboard(translator: Translator) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(translator.get("DELETE_CAPTION"), "delcaption"),
                InlineKeyboardButton(translator.get("CLOSE"), "close"),
            ]
        ]
    )


async def set_caption(_: Client, msg: Message):
    udb = UserDB()
    user_id = msg.from_user.id
    user_locale = udb.get_var("locale", user_id)
    translator = Translator(user_locale)

    parts = msg.text.split(" ", 1)
    caption = parts[1] if len(parts) == 2 else ""

    if not caption:
        old_caption = udb.get_var("caption", msg.from_user.id) or ""
        message_text = (
            translator.get("CAPTION_SET", caption=old_caption)
            if old_caption
            else translator.get("CAPTION_NOT_SET")
        ) + f"\n\n{translator.get('CAPTION_FOOT_NOTE', )}"
    else:
        udb.set_var("caption", caption, msg.from_user.id)
        message_text = (
            translator.get("CAPTION_SET", caption=caption)
            + f"\n\n{translator.get('CAPTION_FOOT_NOTE')}"
        )

    await msg.reply_text(
        message_text, quote=True, reply_markup=get_inline_keyboard(translator)
    )


async def del_caption(_: Client, msg: CallbackQuery):
    udb = UserDB()
    user_id = msg.from_user.id
    user_locale = udb.get_var("locale", user_id)
    translator = Translator(user_locale)

    udb.set_var("caption", "", msg.from_user.id)
    await msg.message.edit_text(
        translator.get("CAPTION_NOT_SET")
        + f"\n\n{translator.get('CAPTION_FOOT_NOTE')}",
        reply_markup=get_inline_keyboard(translator),
    )
