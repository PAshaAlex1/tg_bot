from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class OrderForm(StatesGroup):
    phone = State()
    address = State()
    comment = State()

@router.message(F.text == "Оформить заказ")
async def start_order(message: Message, state: FSMContext):
    await message.answer("Введите ваш телефон для связи:")
    await state.set_state(OrderForm.phone)

@router.message(OrderForm.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите адрес доставки или напишите 'самовывоз':")
    await state.set_state(OrderForm.address)

@router.message(OrderForm.address)
async def get_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Комментарий к заказу (опционально):")
    await state.set_state(OrderForm.comment)

@router.message(OrderForm.comment)
async def get_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    text = (
        f"Ваш заказ:\n"
        f"Телефон: {data.get('phone')}\n"
        f"Адрес/доставка: {data.get('address')}\n"
        f"Комментарий: {data.get('comment')}\n"
        f"\nПроверьте данные и подтвердите заказ.\n"
        f"Для подтверждения отправьте 'Подтвердить'."
    )
    await message.answer(text)
    await state.set_state("confirm")


# Финальное подтверждение заказа и выставление счета
from aiogram.types import LabeledPrice, PreCheckoutQuery, SuccessfulPayment
from bot.config import Config
from bot.services.cart import get_cart_items
from bot.storage import get_item_by_id

@router.message(F.text.lower() == "подтвердить")
async def confirm_order(message: Message, state: FSMContext):
    user_id = message.from_user.id
    cart_items = get_cart_items(user_id)
    if not cart_items:
        await message.answer("Ваша корзина пуста. Невозможно выставить счет.")
        await state.clear()
        return
    # Считаем сумму заказа
    total = 0
    description = ""
    for item in cart_items:
        catalog_item = get_item_by_id(item.item_id)
        if catalog_item:
            price = int(catalog_item.price_per_unit * item.weight * item.quantity)
            total += price
            description += f"{catalog_item.title} {item.weight} кг x {item.quantity}\n"
    prices = [LabeledPrice(label="Заказ", amount=total*100)]
    config = Config.from_env()
    await message.bot.send_invoice(
        message.chat.id,
        title="Оплата заказа",
        description=description,
        payload="order_payment",
        provider_token=config.payment_provider_token or "381764678:TEST:66913",
        currency="RUB",
        prices=prices,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
    )
    await state.clear()

# Обработка успешной оплаты
@router.pre_checkout_query()
async def pre_checkout_query_handler(pre_checkout_query: PreCheckoutQuery, bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@router.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    await message.answer("Спасибо за оплату! Ваш заказ принят и будет обработан.")
