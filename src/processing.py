

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
