import re
from pprint import pprint


def read_cook_book_from_file(filename):
    with open(filename, encoding='utf8') as file:
        cook_book = {}
        last_dish = ''
        for line in file:
            if '|' not in line.strip() and len(line.strip()) and re.match('\D', line.strip()):
                cook_book.setdefault(line.strip(), [])
                last_dish = line.strip()
            elif '|' in line.strip():
                line = line.strip().split(' | ')
                cook_book[last_dish].append({'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]})
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book_from_file('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if list(ingredient.values())[0] in list(shop_list.keys()):
                shop_list[list(ingredient.values())[0]]['quantity'] += int(list(ingredient.values())[1]) * person_count
            else:
                shop_list.setdefault(list(ingredient.values())[0],
                                     {'measure': list(ingredient.values())[2],
                                      'quantity': int(list(ingredient.values())[1]) * person_count
                                      })
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))

# cook_book = {
#  'Омлет': [
#    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#   ]}
# {
#  'Картофель': {'measure': 'кг', 'quantity': 2},
#  'Молоко': {'measure': 'мл', 'quantity': 200},
#  'Помидор': {'measure': 'шт', 'quantity': 4},
#  'Сыр гауда': {'measure': 'г', 'quantity': 200},
#  'Яйцо': {'measure': 'шт', 'quantity': 4},
#  'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
