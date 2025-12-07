from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_category_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Бенто", callback_data="category:Бенто")],
            [InlineKeyboardButton(text="Торты", callback_data="category:Торты")],
            [InlineKeyboardButton(text="Десерты", callback_data="category:Десерты")],
        ]
    )
