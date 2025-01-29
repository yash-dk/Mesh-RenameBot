from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from ..database.user_db import UserDB

foot_note = (
    "NOTE: You can set the caption by sending /setcaption followed by a space and then the caption. "
    "You can include <code>{filename}</code> in the caption to include the filename of the file being renamed."
)


def get_inline_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Delete Caption", "delcaption"),
                InlineKeyboardButton("Close", "close"),
            ]
        ]
    )


async def set_caption(_: Client, msg: Message):
    udb = UserDB()
    parts = msg.text.split(" ", 1)
    caption = parts[1] if len(parts) == 2 else ""

    if not caption:
        old_caption = udb.get_var("caption", msg.from_user.id) or ""
        message_text = (
            f"Your current caption is: {old_caption}"
            if old_caption
            else "No caption set."
        ) + f"\n\n{foot_note}"
    else:
        udb.set_var("caption", caption, msg.from_user.id)
        message_text = f"Caption set to: {caption}\n\n{foot_note}"

    await msg.reply_text(message_text, quote=True, reply_markup=get_inline_keyboard())


async def del_caption(_: Client, msg: CallbackQuery):
    udb = UserDB()
    udb.set_var("caption", "", msg.from_user.id)
    await msg.message.edit_text(
        f"Caption deleted successfully.\n\n{foot_note}",
        reply_markup=get_inline_keyboard(),
    )
