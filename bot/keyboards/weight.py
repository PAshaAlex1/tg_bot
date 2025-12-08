from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.services.catalog import get_item_by_id

def get_weight_keyboard(item_id: int) -> InlineKeyboardMarkup:
    item = get_item_by_id(item_id)
    if not item:
        return InlineKeyboardMarkup(inline_keyboard=[])
    keyboard = [
        [InlineKeyboardButton(text=f"{w} кг", callback_data=f"weight:{item_id}:{w}")]
        for w in item.weights
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
