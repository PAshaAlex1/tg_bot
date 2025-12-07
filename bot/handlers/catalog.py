from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from bot.keyboards.main import get_main_menu
from bot.keyboards.catalog import get_category_keyboard
from bot.services.catalog import get_items_by_category, get_item_by_id

router = Router()

@router.message(F.text == "📦 Каталог")
async def show_catalog_menu(message: Message):
    await message.answer(
        "Выберите категорию:",
        reply_markup=get_category_keyboard()
    )

@router.callback_query(F.data.startswith("category:"))
async def show_category_items(query: CallbackQuery):
    category = query.data.split(":", 1)[1]
    items = get_items_by_category(category)
    if not items:
        text = f"Нет доступных товаров в категории '{category}'."
        await query.message.answer(text)
        await query.answer()
        return
    text = f"Товары категории '{category}':\n\n"
    keyboard = []
    for item in items:
        text += f"{item.title} — {item.price_per_unit:.0f} руб. (Доступные веса: {', '.join(str(w) for w in item.weights)})\n"
        keyboard.append([InlineKeyboardButton(text=f"Подробнее: {item.title}", callback_data=f"item:{item.id}")])
    await query.message.answer(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))
    await query.answer()

@router.callback_query(F.data.startswith("item:"))
async def show_item_card(query: CallbackQuery):
    item_id = int(query.data.split(":", 1)[1])
    item = get_item_by_id(item_id)
    if not item:
        await query.message.answer("Товар не найден")
        await query.answer()
        return
    caption = (
        f"<b>{item.title}</b>\n"
        f"Цена: {item.price_per_unit:.0f} руб.\n"
        f"Доступные веса: {', '.join(str(w) for w in item.weights)} кг\n\n"
        f"{item.description}"
    )
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Добавить в корзину", callback_data=f"addcart:{item.id}")]]
    )
    if item.photo_file_id:
        await query.message.answer_photo(item.photo_file_id, caption=caption, parse_mode="HTML", reply_markup=markup)
    else:
        await query.message.answer(caption, parse_mode="HTML", reply_markup=markup)
    await query.answer()


