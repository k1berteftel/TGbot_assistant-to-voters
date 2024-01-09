from aiogram import Bot
from aiogram.types import BotCommand
from election_bot_project.Lexicon.messages import messages

# import lexicon для команды и ее описания

async def set_menu(bot: Bot) -> None:
    menu_list = [BotCommand(command="/start", description=messages["/start"])]
    await bot.set_my_commands(menu_list)
