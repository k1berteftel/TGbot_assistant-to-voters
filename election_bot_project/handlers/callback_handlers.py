from aiogram import Router
from aiogram.types import CallbackQuery
from election_bot_project.Lexicon.messages import buttons
from election_bot_project.keyboard.in_botton import back_btn, builder
from election_bot_project.Lexicon.messages import messages

clb_router = Router()


@clb_router.callback_query(lambda msg: msg.data == buttons["Советы"])
async def press_help(clb: CallbackQuery):
    await clb.message.edit_text(text="помощь", reply_markup=back_btn)


@clb_router.callback_query(lambda msg: msg.data == buttons["Информация"])
async def press_help(clb: CallbackQuery):
    await clb.message.edit_text(text="помощь", reply_markup=back_btn)


@clb_router.callback_query(lambda msg: msg.data == buttons["Вопрос-ответ"])
async def press_help(clb: CallbackQuery):
    await clb.message.edit_text(text="помощь", reply_markup=back_btn)


@clb_router.callback_query(lambda msg: msg.data == buttons["Памятка избирателя"])
async def press_help(clb: CallbackQuery):
    await clb.message.edit_text(text="помощь", reply_markup=back_btn)


@clb_router.callback_query(lambda msg: msg.data == "back")
async def back_to_menu(clb: CallbackQuery):
    await clb.message.edit_text(text=messages["hello"], reply_markup=builder.as_markup())
