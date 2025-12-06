from aiogram import Router
from aiogram.types import Message
from bot.keyboards.main import get_main_menu

router = Router()

@router.message(lambda message: message.text == "📦 Каталог")
async def show_catalog(message: Message):
    await message.answer(
        "📦 Каталог товаров\n\n"
        "Выберите категорию:",
        reply_markup=get_main_menu()
    )

