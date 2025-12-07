from dataclasses import dataclass
from typing import List

@dataclass
class CatalogItem:
    id: int
    title: str
    description: str
    category: str  # "Бенто", "Торты", "Десерты"
    price_per_unit: float
    weights: List[float]
    photo_file_id: str
    available: bool = True

# Примитивный in-memory каталог: 3 на категорию
_catalog: List[CatalogItem] = [
    # Бенто
    CatalogItem(
        id=1,
        title="Молочная девочка",
        description="Коржи на сгущенном молоке; молочная пропитка; малиновая начинка",
        category="Бенто",
        price_per_unit=500.0,
        weights=[0.5, 0.75],
        photo_file_id="",
    ),
    CatalogItem(
        id=2,
        title="Бенто Манго",
        description="Лёгкий крем и цедра манго. Отлично подойдёт ребёнку.",
        category="Бенто",
        price_per_unit=850.0,
        weights=[0.4, 0.5],
        photo_file_id="",
    ),
    CatalogItem(
        id=3,
        title="Бенто Клубника",
        description="Свежие ягоды и мягкий бисквит, классика лета.",
        category="Бенто",
        price_per_unit=950.0,
        weights=[0.35, 0.5],
        photo_file_id="",
    ),
    # Торты
    CatalogItem(
        id=4,
        title="Торт Шоколадный",
        description="Классика: шоколадный торт с ганашем.",
        category="Торты",
        price_per_unit=1800.0,
        weights=[1.0, 1.5, 2.0],
        photo_file_id="",
    ),
    CatalogItem(
        id=5,
        title="Торт Медовик",
        description="Нежный медовый бисквит с кремом из сгущенки.",
        category="Торты",
        price_per_unit=1700.0,
        weights=[1.0, 1.5],
        photo_file_id="",
    ),
    CatalogItem(
        id=6,
        title="Торт Птичье молоко",
        description="Легендарное суфле в глазури. Любим взрослыми.",
        category="Торты",
        price_per_unit=2000.0,
        weights=[1.0, 2.0],
        photo_file_id="",
    ),
    # Десерты
    CatalogItem(
        id=7,
        title="Десерт Панна Котта",
        description="Кремовый сливочный десерт с ягодами.",
        category="Десерты",
        price_per_unit=220.0,
        weights=[0.2],
        photo_file_id="",
    ),
    CatalogItem(
        id=8,
        title="Десерт Тирамису",
        description="Итальянский десерт в баночке, с настоящим кофе.",
        category="Десерты",
        price_per_unit=290.0,
        weights=[0.25],
        photo_file_id="",
    ),
    CatalogItem(
        id=9,
        title="Десерт Мусс Манго",
        description="Лёгкий мусс с манго, старт сезона.",
        category="Десерты",
        price_per_unit=250.0,
        weights=[0.2],
        photo_file_id="",
    ),
]

def get_catalog() -> List[CatalogItem]:
    return _catalog

def get_categories() -> List[str]:
    return ["Бенто", "Торты", "Десерты"]
