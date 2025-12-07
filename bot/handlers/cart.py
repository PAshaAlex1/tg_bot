from aiogram import Router
from aiogram.types import Message
from bot.keyboards.main import get_main_menu

router = Router()

@router.message(lambda message: message.text == "🛒 Корзина")
async def show_cart(message: Message):
    await message.answer(
        "🛒 Ваша корзина пуста",
        reply_markup=get_main_menu()
    )


