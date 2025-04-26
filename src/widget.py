from masks import get_mask_card_number
from masks import get_mask_account
import re

def mask_account_card(card_name: str) -> str:
    if "Visa" in card_name or "Maestro" in card_name:
        card_number = ''
        card_type = ''
        for symbol in card_name:
            if symbol.isdigit():
                card_number+=symbol
            else:
                card_type+=symbol
        card_number_mask = get_mask_card_number(card_number)
        return f"{card_type}{card_number_mask}"
    else:
        if "Счет" in card_name:
            account_number = ''
            for symbol in card_name:
                if symbol.isdigit():
                    account_number+=symbol
            card_account_mask = get_mask_account(account_number)
        return f"Счет {card_account_mask}"

print(mask_account_card(card_name="Счет 73654108430135874305"))
