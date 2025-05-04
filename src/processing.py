# -*- coding: utf-8 -*-


def filter_by_state(card_data: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и значение ключа,
    возвращает только список словарей с заданным ключом"""
    new_card_data = []
    for data in card_data:
        if data["state"] == state:
            new_card_data.append(data)
    return new_card_data


def sort_by_date(card_data: list, order_for_sort: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
        задающий порядок сортировки (по умолчанию — убывание).
        Функция должна возвращать новый список, отсортированный по дате (
    date)"""
    return sorted(card_data, key=lambda data: data.get("date", 0), reverse=order_for_sort)


card_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
state = ""
order_for_sort = False
print(filter_by_state(card_data, state))
print(sort_by_date(card_data, order_for_sort))
