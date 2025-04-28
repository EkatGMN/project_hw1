

def filter_by_state(my_data: list, state='EXECUTED') -> list:
    """Функция принимает список словарей и значение ключа,
     возвращает только список словарей с заданным ключом"""
    new_list = []
    for i in my_data:
        if i['state'] == state:
            new_list.append(i)
    return new_list



my_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
state = 'CANCELED'
print(filter_by_state(my_data, state))


def sort_by_date(my_list: list, order_for_sort=True)-> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (
date)"""
    return sorted(my_list, key=lambda item: item.get('date', 0), reverse = order_for_sort)

my_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

print(sort_by_date(my_list))