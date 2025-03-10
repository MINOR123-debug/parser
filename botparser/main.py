import sys
import asyncio
import logging
import signal
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from cryptography.hazmat.backends import default_backend
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.command_handlers import command_router
from help import router
from rik import routeradm
from creit import creit_router
from admin import router11
from parser2 import parser_router, setup_telethon

# Логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    # Ініціалізація Telethon (перенесено в окрему функцію)
    await setup_telethon()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Підключення роутерів
    dp.include_router(parser_router)
    dp.include_router(command_router)
    dp.include_router(router)
    dp.include_router(routeradm)
    dp.include_router(creit_router)
    dp.include_router(router11)

    logger.info("Бот запускається...")

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Помилка під час роботи бота: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        # Використовуємо asyncio.run() для основного циклу
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот вимкнено вручну.")
