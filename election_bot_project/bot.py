import asyncio

from aiogram import Bot, Dispatcher
from Config_data.Config import Config, load_config
from handlers.main_handlers import router
from handlers.callback_handlers import clb_router

from keyboard.menu import set_menu


# Тут будут импортированны хендлеры

async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(router)
    dp.include_router(clb_router)
    await set_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
