
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot.services.cart import add_to_cart, get_cart_items, remove_from_cart, clear_cart
from bot.services.catalog import get_item_by_id
from bot.keyboards.catalog_quantity import get_quantity_keyboard
from bot.keyboards.main import get_main_menu
from bot.keyboards.cart import get_cart_actions_keyboard
from bot.keyboards.weight import get_weight_keyboard

router = Router()

# Handler для удаления позиции из корзины
@router.callback_query(F.data.startswith("delcart:"))
async def delete_cart_item(query: CallbackQuery):
    _, item_id, weight = query.data.split(":")
    item_id = int(item_id)
    weight = float(weight)
    user_id = query.from_user.id
    remove_from_cart(user_id, item_id, weight)
    await query.message.answer("Позиция удалена из корзины.")
    await query.answer()

# Handler для полной очистки корзины
@router.callback_query(F.data == "clearcart")
async def clear_user_cart(query: CallbackQuery):
    user_id = query.from_user.id
    clear_cart(user_id)
    await query.message.answer("Корзина очищена.")
    await query.answer()


@router.message(lambda message: message.text == "🛒 Корзина")
async def show_cart(message: Message):
    user_id = message.from_user.id
    items = get_cart_items(user_id)
    if not items:
        await message.answer(
            "🛒 Ваша корзина пуста",
            reply_markup=get_main_menu()
        )
        return
    text = "🛒 Ваша корзина:\n\n"
    for cart_item in items:
        catalog_item = get_item_by_id(cart_item.item_id)
        title = catalog_item.title if catalog_item else f"ID {cart_item.item_id}"
        text += f"{title}, вес: {cart_item.weight} кг, количество: {cart_item.quantity}\n"
    await message.answer(text, reply_markup=get_cart_actions_keyboard(items))

# Handler для выбора веса товара после нажатия "Добавить в корзину"
# Handler для выбора веса товара после нажатия "Добавить в корзину"
@router.callback_query(F.data.startswith("addcart:"))
async def choose_weight(query: CallbackQuery):
    item_id = int(query.data.split(":", 1)[1])
    await query.message.answer(
        "Выберите вес товара:",
        reply_markup=get_weight_keyboard(item_id)
    )
    await query.answer()

# Handler для выбора количества после выбора веса
# Handler для выбора количества после выбора веса
@router.callback_query(F.data.startswith("weight:"))
async def choose_quantity(query: CallbackQuery):
    _, item_id, weight = query.data.split(":")
    item_id = int(item_id)
    weight = float(weight)
    await query.message.answer(
        "Выберите количество:",
        reply_markup=get_quantity_keyboard(item_id, weight)
    )
    await query.answer()

# Handler для добавления товара в корзину после выбора количества
@router.callback_query(F.data.startswith("quantity:"))
async def add_item_to_cart(query: CallbackQuery):
    _, item_id, weight, quantity = query.data.split(":")
    item_id = int(item_id)
    weight = float(weight)
    quantity = int(quantity)
    user_id = query.from_user.id
    add_to_cart(user_id, item_id, weight, quantity)
    await query.message.answer("Товар добавлен в корзину! 🛒")
    await query.answer()




