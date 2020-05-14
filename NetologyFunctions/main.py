def print_name_by_doc_number(number):
    for document in documents:
        if document["number"] == number:
            return (document["name"])
    return ('Документа с таким номером нет.')


def print_directory_by_doc_number(number):
    for shelf in directories:
        if number in directories[shelf]:
            return (shelf)
    return ('Документа с таким номером нет.')


def print_doc_list():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def print_shelf_list():
    for shelf in directories.items():
        shelf_number, doc_list = shelf
        print(f'{shelf_number}: ', end='')
        for item in doc_list:
            print(f'[{item}]', end='')
        print()


def add_new_doc(number, doc_type, name, shelf):
    if check_shelf_exist(shelf):
        documents.append({"type": doc_type, "number": number, "name": name})
        directories[shelf].append(number)
        print('Документ добавлен.')
    else:
        print('Полка не найдена, документ не добавлен.')


def check_shelf_exist(shelf):
    return shelf in directories


def check_doc_exist(number):
    for document in documents:
        if number in document.values():
            return True
    return False


def check_doc_in_shelf_exist(number):
    for value in directories.values():
        if number in value:
            return True
    return False


def delete_doc(number):
    if check_doc_exist(number) and check_doc_in_shelf_exist(number):
        for document in documents:
            if document["number"] == number:
                documents.remove(document)
        for shelf in directories:
            if number in directories[shelf]:
                directories[shelf].remove(number)
        print('Документ успешно удалён.')
    else:
        print('Документ не найден.')


def move_doc(number, target_shelf):
    if check_doc_exist(number):
        if check_shelf_exist(target_shelf):
            for shelf in directories:
                if number in directories[shelf]:
                    directories[shelf].remove(number)
                    directories[target_shelf].append(number)
            print(f'Документ {number} перенесен на полку {target_shelf}.')
        else:
            print('Неверный номер полки.')
    else:
        print('Неверный номер документа.')


def add_shelf(shelf):
    if not check_shelf_exist(shelf):
        directories[shelf] = []
    else:
        print('Полка с таким номером уже существует.')


def print_name_list():
    for document in documents:
        try:
            print(f'"{document["name"]}"')
        except KeyError:
            print('Документ не подписан.')



def print_options():
    print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;')
    print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;')
    print('dl – document list – команда, которая выведет список всех документов;')
    print('sl - shelf list - команда, которая выведет список документов на полках;')
    print('nl - name list - команда, которая выведет список имен')
    print(
        'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;')
    print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;')
    print(
        'm – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;')
    print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;')
    print('Для завершения работы с программой введите q.\n')
    print('Введите опцию:\n')

def main():
    print('Программный комплекс "Секретарь 3000"')
    print('Добро пожаловать!')
    print()

    while True:
        print_options()
        user_input = input('> ')
        print()

        if user_input == 'p':
            user_input = input('Введите номер документа: ')
            print('Имя человека:', print_name_by_doc_number(user_input))
            print()

        elif user_input == 's':
            user_input = input('Введите номер документа: ')
            print('Номер полки:', print_directory_by_doc_number(user_input))
            print()

        elif user_input == 'dl':
            print('Список всех документов:\n')
            print_doc_list()
            print()

        elif user_input == 'sl':
            print('Список всех документов на полках:\n')
            print_shelf_list()
            print()

        elif user_input == 'nl':
            print('Список всех имён:\n')
            print_name_list()
            print()

        elif user_input == 'a':
            add_new_doc(input('Введите номер документа: '),
                        input('Введите тип документа: '),
                        input('Введите имя владельца: '),
                        input('Введите номер полки для хранения: '))
            print()

        elif user_input == 'd':
            delete_doc(input('Введите номер документа: '))
            print()

        elif user_input == 'm':
            move_doc(input('Введите номер документа, который нужно перенести: '),
                     input('Введите целевую полку: '))
            print()

        elif user_input == 'as':
            add_shelf(input('Введите номер новой полки:'))
            print()

        elif user_input == 'q':
            break

        else:
            print('Такой команды нет.\n')


documents = [
    {"type": "passport", "number": "2207 876234"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

main()