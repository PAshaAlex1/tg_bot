from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards.main import get_main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в магазин тортов!\n\n"
        "Здесь вы можете выбрать и заказать вкусные торты.",
        reply_markup=get_main_menu()
    )

