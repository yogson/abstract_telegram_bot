from typing import Callable, Coroutine

from telegram import Update
from telegram.ext import ContextTypes


class HandlersChain:
    def __init__(self, *args: Callable[[Update, ContextTypes.DEFAULT_TYPE], Coroutine]):
        self.handlers = args

    def __call__(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        return self._coroutine(update, context)

    async def _coroutine(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        for handler in self.handlers:
            await handler(update, context)
