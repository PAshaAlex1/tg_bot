from bot.storage import CatalogItem, get_catalog
from typing import List, Optional

def get_items_by_category(category: str) -> List[CatalogItem]:
    """Возвращает товары заданной категории (по названию категории)"""
    return [item for item in get_catalog() if item.category == category and item.available]

def get_item_by_id(item_id: int) -> Optional[CatalogItem]:
    for item in get_catalog():
        if item.id == item_id:
            return item
    return None
