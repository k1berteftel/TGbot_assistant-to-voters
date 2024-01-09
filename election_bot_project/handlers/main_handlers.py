from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from election_bot_project.Lexicon.messages import messages
from election_bot_project.keyboard.in_botton import builder




router = Router()


@router.message(CommandStart())
async def hello_menu(message: Message):
    await message.answer(text=messages["hello"], reply_markup=builder.as_markup())

@router.message()
async def random_message(message: Message):
    await message.answer(text=messages["Сообщение"])