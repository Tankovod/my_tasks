from src.config.bot import bot
from bot.core.handlers.commands import start
from bot.core.handlers.registration import handle_registration

bot.add_handler(start)
bot.add_handler(handle_registration)

if __name__ == "__main__":
    bot.run()
