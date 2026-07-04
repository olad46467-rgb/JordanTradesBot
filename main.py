import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.admin import router as admin_router


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(admin_router)

    print("✅ JordanTradesBot is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
