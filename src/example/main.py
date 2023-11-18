from example.handlers.echo_handler import chain, kek
from sdk.tg.bot import Bot
from sdk.tg.common import Command, BilingualString, Lang

Bot.api_token = "6907111185:AAFW1N-aX4APTO98aOZEdy2HNjzgyXyovz4"
bot = Bot()

bot.commands = {
    Command(
        name="boot",
        description=BilingualString(eng="Let's boot some...", rus="Давайте загрузим немного..."),
        handler=chain),
    Command(
        name="go",
        description=BilingualString(eng="Go!", rus="Погнали!"),
        handler=chain),
    Command(
        name="stop",
        description=BilingualString(eng="Enough!", rus="Харэ"),
        handler=chain),
    Command(
        name="zai",
        description=BilingualString(eng="Zai!", rus="Дзай дзай"),
        handler=kek),
}

bot.set_main_menu(lang=Lang.rus)
bot.run()

