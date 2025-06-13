import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router

TOKEN = '8190188550:AAE_Y4jwVLJqPlFh58BcB7Vg9KR05rJlO3Y'


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')