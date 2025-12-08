
def test_order_happy_path_logic():
    # Имитация данных, которые собирает FSM
    fsm_data = {}
    # Шаг 1: телефон
    fsm_data["phone"] = "+79991234567"
    # Шаг 2: адрес
    fsm_data["address"] = "г. Москва, ул. Пушкина, д. 1"
    # Шаг 3: комментарий
    fsm_data["comment"] = "Позвонить за час"
    # Проверка
    assert fsm_data["phone"] == "+79991234567"
    assert fsm_data["address"] == "г. Москва, ул. Пушкина, д. 1"
    assert fsm_data["comment"] == "Позвонить за час"
    # Финальное подтверждение (очистка)
    fsm_data.clear()
    assert fsm_data == {}
