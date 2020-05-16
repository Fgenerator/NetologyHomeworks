import re


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


# cook_book = {
#  'Омлет': [
#    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#   ]}
def get_shop_list_by_dishes(dishes, person_count):
    ...


print(read_cook_book_from_file('recipes.txt'))