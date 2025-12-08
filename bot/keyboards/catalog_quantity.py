from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_quantity_keyboard(item_id: int, weight: float) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text=str(q), callback_data=f"quantity:{item_id}:{weight}:{q}")]
        for q in range(1, 6)
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
