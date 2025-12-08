
import logging
from aiogram import Router, F
from aiogram.types import Message
from bot.storage import CatalogItem, _catalog

router = Router()

ADMIN_IDS = [8197814475]  # Замените на свой Telegram ID
logger = logging.getLogger(__name__)

@router.message()
async def debug_all(message: Message):
    logger.info(f"DEBUG: message from {message.from_user.id}: {message.text}")

@router.message(F.text.startswith("/edit_item"))
async def edit_item(message: Message):
    logger.info(f"edit_item called by user {message.from_user.id}: {message.text}")
    if message.from_user.id not in ADMIN_IDS:
        await message.answer(f"Нет прав администратора. Ваш ID: {message.from_user.id}")
        return
    try:
        # Пример: /edit_item 5|1500|1.0,2.0|True
        parts = message.text[len("/edit_item "):].split("|")
        item_id = int(parts[0])
        price = float(parts[1])
        weights = [float(w) for w in parts[2].split(",")]
        available = parts[3].strip().lower() in ("true", "1", "yes", "да")
        for item in _catalog:
            if item.id == item_id:
                item.price_per_unit = price
                item.weights = weights
                item.available = available
                await message.answer(f"Товар ID {item_id} обновлён.")
                logger.info(f"Item {item_id} updated: price={price}, weights={weights}, available={available}")
                return
        await message.answer("Товар не найден.")
        logger.warning(f"Item {item_id} not found for edit.")
    except Exception as e:
        await message.answer(f"Ошибка редактирования: {e}")
        logger.error(f"Ошибка редактирования: {e}")
# ...existing code...

# Debug handler должен быть последним!
@router.message()
async def debug_all(message: Message):
    logger.info(f"DEBUG: message from {message.from_user.id}: {message.text}")

@router.message(F.text.startswith("/add_item "))
async def add_item(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Нет прав администратора.")
        return
    try:
        # Пример: /add_item Торт Сметанник|Торты|1200|1.0,1.5|Описание
        parts = message.text[len("/add_item "):].split("|")
        title, category, price, weights, description = parts
        price = float(price)
        weights = [float(w) for w in weights.split(",")]
        item_id = max([i.id for i in _catalog], default=0) + 1
        _catalog.append(CatalogItem(
            id=item_id,
            title=title,
            description=description,
            category=category,
            price_per_unit=price,
            weights=weights,
            photo_file_id="",
            available=True
        ))
        await message.answer(f"Товар '{title}' добавлен.")
    except Exception as e:
        await message.answer(f"Ошибка добавления: {e}")

@router.message(F.text.startswith("/archive_item "))
async def archive_item(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Нет прав администратора.")
        return
    try:
        item_id = int(message.text[len("/archive_item "):])
        for item in _catalog:
            if item.id == item_id:
                item.available = False
                await message.answer(f"Товар ID {item_id} архивирован.")
                return
        await message.answer("Товар не найден.")
    except Exception as e:
        await message.answer(f"Ошибка архивирования: {e}")
