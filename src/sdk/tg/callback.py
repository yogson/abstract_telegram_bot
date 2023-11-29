from telegram import Update
from telegram.ext import ContextTypes


async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer(text=query.data)
    await query.delete_message()
