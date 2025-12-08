from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_cart_actions_keyboard(items):
    keyboard = []
    for item in items:
        keyboard.append([
            InlineKeyboardButton(
                text=f"Удалить: {item.weight} кг x {item.quantity}",
                callback_data=f"delcart:{item.item_id}:{item.weight}"
            )
        ])
    if items:
        keyboard.append([
            InlineKeyboardButton(text="Очистить корзину", callback_data="clearcart")
        ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
