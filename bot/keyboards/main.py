from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu() -> ReplyKeyboardMarkup:
    """Главное меню с кнопками категорий."""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📦 Каталог")],
            [KeyboardButton(text="🛒 Корзина")],
        ],
        resize_keyboard=True
    )
    return keyboard




