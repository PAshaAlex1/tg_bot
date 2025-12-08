from typing import Dict, Optional, List
from bot.storage import Cart, CartItem

# In-memory хранилище корзин: user_id -> Cart
carts: Dict[int, Cart] = {}

def get_cart(user_id: int) -> Cart:
    """Получить корзину пользователя, создать если нет."""
    if user_id not in carts:
        carts[user_id] = Cart(user_id=user_id, items=[])
    return carts[user_id]

def add_to_cart(user_id: int, item_id: int, weight: float, quantity: int) -> None:
    """Добавить позицию в корзину пользователя (KISS: если такая уже есть — увеличить количество)."""
    cart = get_cart(user_id)
    for cart_item in cart.items:
        if cart_item.item_id == item_id and cart_item.weight == weight:
            cart_item.quantity += quantity
            return
    cart.items.append(CartItem(item_id=item_id, weight=weight, quantity=quantity))

def remove_from_cart(user_id: int, item_id: int, weight: float) -> None:
    """Удалить позицию из корзины по item_id и weight."""
    cart = get_cart(user_id)
    cart.items = [ci for ci in cart.items if not (ci.item_id == item_id and ci.weight == weight)]

def clear_cart(user_id: int) -> None:
    """Очистить корзину пользователя."""
    if user_id in carts:
        carts[user_id].items.clear()

def get_cart_items(user_id: int) -> List[CartItem]:
    """Получить все позиции корзины пользователя."""
    return get_cart(user_id).items
