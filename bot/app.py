import logging
import asyncio
from aiogram import Bot, Dispatcher
from bot.config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    config = Config.from_env()
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    
    logger.info("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

