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

# Финальное подтверждение заказа
@router.message(F.text.lower() == "подтвердить")
async def confirm_order(message: Message, state: FSMContext):
    await message.answer("Спасибо! Ваш заказ принят и будет обработан.")
    await state.clear()
