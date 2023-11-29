from functools import partial
from typing import Coroutine, Any

from telegram.ext import ContextTypes

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def _inline_keyboard_button(txt: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(txt, callback_data=txt)


def _build_from_list(data: list[str | tuple[str]], inline=True, one_time=True) -> ReplyKeyboardMarkup:
    if inline:
        button_class = _inline_keyboard_button
        kb_class = InlineKeyboardMarkup
    else:
        button_class = KeyboardButton
        kb_class = partial(ReplyKeyboardMarkup, one_time_keyboard=one_time)
    keys = [
        (button_class(item),) if isinstance(item, str) else [button_class(subitem) for subitem in item] for item in data
    ]
    return kb_class(keys)


async def _show_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    *,
    buttons: list[str | tuple[str]],
    text: str,
    inline: bool,
    one_time: bool
):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=_build_from_list(
            buttons,
            inline=inline,
            one_time=one_time
        ),
    )


def keyboard_handler(
    *, text: str, buttons: list[str | tuple[str]], inline=True, one_time=True
) -> partial[Coroutine[Any, Any, None]]:
    return partial(_show_keyboard, text=text, buttons=buttons, inline=inline, one_time=one_time)
