from telegram import Update
from telegram.ext import ContextTypes

from sdk.tg.bot import Bot
from sdk.tg.common import Lang
from sdk.tg.handlers import HandlersChain


async def lol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="LOL!")


async def kek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    instance: Bot = context.application.bot_data["instance"]
    await instance.update_main_menu(lang=Lang(update.effective_user.language_code), update=update)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Kek!")


chain = HandlersChain(lol, kek)
