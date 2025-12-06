import logging
import asyncio
from aiogram import Bot, Dispatcher
from bot.config import Config
from bot.handlers import start, catalog, cart

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    try:
        config = Config.from_env()
        bot = Bot(token=config.bot_token)
        dp = Dispatcher()
        
        dp.include_router(start.router)
        dp.include_router(catalog.router)
        dp.include_router(cart.router)
        
        logger.info("Бот запущен")
        await dp.start_polling(bot, skip_updates=True)
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Ошибка при работе бота: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    asyncio.run(main())

