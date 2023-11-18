from telegram import Update
from telegram.ext import ContextTypes

from sdk.tg.handlers import HandlersChain


async def lol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="LOL!")


async def kek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Kek!")


chain = HandlersChain(lol, kek)
