import pytest
from bot.services.cart import add_to_cart, get_cart_items, clear_cart, remove_from_cart

def test_cart_happy_path():
    user_id = 12345
    item_id = 1
    weight = 0.5
    quantity = 2
    clear_cart(user_id)
    # Добавление
    add_to_cart(user_id, item_id, weight, quantity)
    items = get_cart_items(user_id)
    assert len(items) == 1
    assert items[0].item_id == item_id
    assert items[0].weight == weight
    assert items[0].quantity == quantity
    # Удаление позиции
    remove_from_cart(user_id, item_id, weight)
    items = get_cart_items(user_id)
    assert len(items) == 0
    # Добавление двух позиций и очистка
    add_to_cart(user_id, item_id, weight, 1)
    add_to_cart(user_id, item_id, 0.75, 1)
    items = get_cart_items(user_id)
    assert len(items) == 2
    clear_cart(user_id)
    items = get_cart_items(user_id)
    assert len(items) == 0
