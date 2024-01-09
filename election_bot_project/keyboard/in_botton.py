from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from election_bot_project.Lexicon.messages import buttons

builder = InlineKeyboardBuilder()
button_list: list[InlineKeyboardButton] = [InlineKeyboardButton(text=key, callback_data=clb) for key, clb in buttons.items()]
builder.row(*button_list, width=2)

button = InlineKeyboardButton(text="На главное меню", callback_data="back")
back_btn = InlineKeyboardMarkup(inline_keyboard=[[button]])
