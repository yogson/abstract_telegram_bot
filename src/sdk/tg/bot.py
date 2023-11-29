import asyncio

import uvloop

from telegram import BotCommand, Update, BotCommandScopeChat
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
)

from sdk.tg.callback import callback
from sdk.tg.common import Command, Lang
from sdk.tg.exceptions import NoApiTokenError


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


class Bot:
    api_token: str = None
    _instance = None

    def __new__(cls):
        if not cls.api_token:
            raise NoApiTokenError()
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.app: Application = ApplicationBuilder().token(self.api_token).build()
        self.commands: set[Command] = set()

    def set_main_menu(self, lang=Lang.eng, update: Update = None):
        asyncio.get_event_loop().run_until_complete(self.update_main_menu(lang, update))

    async def update_main_menu(self, lang: Lang = None, update: Update = None):
        return await self.app.bot.set_my_commands(
            commands=(BotCommand(cmd.name, getattr(cmd.description, lang.value)) for cmd in self.commands),
            scope=BotCommandScopeChat(chat_id=update.effective_chat.id) if update else None,
        )

    def _reg_commands(self):
        for cmd in self.commands:
            self.app.add_handler(CommandHandler(cmd.name, cmd.handler))

    def _reg_callback(self, handler=callback):
        self.app.add_handler(CallbackQueryHandler(handler))

    def run(self):
        self._reg_callback()
        self._reg_commands()
        self.app.bot_data["instance"] = self
        self.app.run_polling()
