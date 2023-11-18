import asyncio

from telegram import BotCommand
from telegram.ext import Application, ApplicationBuilder, CommandHandler

from sdk.tg.common import Command, Lang
from sdk.tg.exceptions import NoApiTokenError


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

    def set_main_menu(self, lang=Lang.eng):
        loop.run_until_complete(self._set_main_menu(lang))

    async def _set_main_menu(self, lang: Lang):
        await self.app.bot.set_my_commands(
            commands=(BotCommand(cmd.name, getattr(cmd.description, lang.value)) for cmd in self.commands)
        )

    def _reg_commands(self):
        for cmd in self.commands:
            self.app.add_handler(CommandHandler(cmd.name, cmd.handler))

    def run(self):
        self._reg_commands()
        self.app.run_polling()

