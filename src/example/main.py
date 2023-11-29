from functools import partial

from example.handlers.echo_handler import kek
from sdk.tg.bot import Bot
from sdk.tg.common import Command, BilingualString, Lang
from sdk.tg.keyboard import keyboard_handler

Bot.api_token = "6907111185:AAFW1N-aX4APTO98aOZEdy2HNjzgyXyovz4"
bot = Bot()

buttons = [
    "Привет медвед 🐻",
    "Отправить посылку 📦",
    ("Уйти в загул", "Получить люлей"),
    "Получить презент 🎁",
    "Закрыть ворота",
    "Заглянуть в жерло вулкана",
]
text = " Чего желаешь?"

bot.commands = {
    Command(
        name="boot",
        description=BilingualString(en="Let's boot some...", ru="Давайте загрузим немного..."),
        handler=kek,
    ),
    Command(
        name="go",
        description=BilingualString(en="Go!", ru="Погнали!"),
        handler=keyboard_handler(text=text, buttons=buttons, inline=False),
    ),
    Command(
        name="stop",
        description=BilingualString(en="Enough!", ru="Харэ"),
        handler=keyboard_handler(text=text, buttons=buttons),
    ),
}

bot.set_main_menu(lang=Lang.eng)
bot.run()
