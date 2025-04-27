from masks import get_mask_card_number
from masks import get_mask_account
import re


def mask_account_card(card_name: str) -> str:
    """Функция принимает тип и номер карты или счета,
     маскирует номер карты (пример вывода Visa Platinum 7000 79** **** 6361)
     и номер счета (пример вывода: Счет **4305)"""
    if "Visa" in card_name or "Maestro" in card_name:
        card_number = ""
        card_type = ""
        for symbol in card_name:
            if symbol.isdigit():
                card_number += symbol
            else:
                card_type += symbol
        card_number_mask = get_mask_card_number(card_number)
        return f"{card_type}{card_number_mask}"
    else:
        if "Счет" in card_name:
            account_number = ""
            for symbol in card_name:
                if symbol.isdigit():
                    account_number += symbol
            card_account_mask = get_mask_account(account_number)
        return f"Счет {card_account_mask}"


def get_date(date: str) -> str:
    """Функция преобразует дату в формате в формате
"2024-03-11T02:26:18.671407" в дату ДД.ММ.ГГГГ"""
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})T.*", date)
    if match:
        year, month, day = match.groups()
        return f"{day}.{month}.{year}"
    else:
        return "Неверный формат"


print(mask_account_card(card_name="Счет 73654108430135874305"))
print(get_date(date="2024-03-12T02:26:18.67"))
