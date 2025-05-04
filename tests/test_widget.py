import pytest
from src.widget import mask_account_card
from src.widget import get_date

"""Тестирует функцию, которая принимает и маскирует номер карты или счета.
Проверка распозавания номера карты/счета;
если введено меньше символов;
если передано пустое значение"""

@pytest.mark.parametrize('card_name, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
    ('', 'Введен неверный номер'),
])

def test_mask_account_card(card_name, expected):
    assert mask_account_card(card_name) == expected


"""Тестирует дату, проверяет:
если введено корректное значение даты,
если передано неверное значение даты"""

@pytest.mark.parametrize('date, expected', [
    ('2024-12-12T02:26:18.67', '12.12.2024'),
    ('2024-13-12T02:26:18.67', 'Неверный формат'),
])

def test_get_date(date, expected):
    assert get_date(date) == expected

