import textwrap

class Contact:
    def __init__(self,
                 first_name: str, second_name: str, phone: str,
                 *args,
                 favorite=False,
                 **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.favorite = favorite
        self.addition_args = args
        self.addition_kwargs = kwargs

    def __str__(self):
        first_name_str = f'First name: {self.first_name}\n'
        second_name_str = f'Second name: {self.second_name}\n'
        phone_str = f'Phone name: {self.phone}\n'
        is_favorite_str = f'Favorite: {self.is_favorite()}\n'
        additional_str = f'{self.type_additional()}\n'
        return first_name_str + second_name_str + phone_str + is_favorite_str + additional_str

    def is_favorite(self):
        if self.favorite:
            return 'Yes'
        else:
            return 'No'

    def type_additional(self):
        result = 'Additional:'
        for arg in self.addition_args:
            result = f'{result}\n\t{arg}'
        for key, value in self.addition_kwargs.items():
            result = f'{result}\n\t{key} : {value}'
        return result


class PhoneBook:
    def __init__(self, name: str):
        self.name = name
        self.contacts = []

    def add_contact(self, new_contact: Contact):
        result = [contact for contact in self.contacts
                  if contact.phone == new_contact.phone]
        if len(result):
            for contact in result:
                print(f'Contact {contact.first_name} {contact.second_name} '
                      f'with phone {contact.phone} already in phonebook {self.name}.\n')
        else:
            self.contacts.append(new_contact)
            print(f'{new_contact.first_name} {new_contact.second_name} added in phonebook {self.name}\n')

    def print_contacts(self):
        print(f'Contacts in phonebook {self.name}:\n')
        for contact in self.contacts:
            print(contact)

    def delete_by_phone(self, phone):
        result = [contact for contact in self.contacts
                  if contact.phone == phone]
        if len(result):
            for contact in result:
                self.contacts.remove(contact)
                print(f'Contact {contact.first_name} {contact.second_name} with phone {phone} deleted.\n')
        else:
            print(f'{phone} not in phonebook {self.name}\n')

    def print_favorites(self):
        result = [contact for contact in self.contacts
                  if contact.favorite]
        if len(result):
            print(f'Favorites contacts in phonebook {self.name}:\n')
            for contact in result:
                print(contact)
        else:
            print(f'No favorites in phonebook {self.name}\n')

    def search_by_name(self, first_name, second_name):
        print(f'Search by name {first_name} {second_name}:')
        result = [contact for contact in self.contacts
                  if (contact.first_name == first_name) and (contact.second_name == second_name)]
        if len(result):
            for contact in result:
                print(contact)
        else:
            print(f'{first_name} {second_name} not in phonebook {self.name}\n')


def prepare_lines(string, max_line):
    list = textwrap.wrap(string, max_line)
    result = ''
    for string in list:
        result += string + '\n'
    return result


def adv_print(*args, **kwargs):
    if kwargs['start']:
        result = kwargs['start']
    else:
        result = ''

    if kwargs['max_line'] >= 0:
        max_line = kwargs['max_line']

    args = (str(arg) for arg in args)
    for line in args:
        result += line
    if max_line > 0:
        result = prepare_lines(result, max_line)

    if kwargs['in_file']:
        with open('result.txt', 'w', encoding='utf8') as rfile:
            rfile.write(result)
    print(result)

# *3. Продвинутый print (необязательное задание)
# Разработать свою реализацию функции print - adv_print. Она ничем не должна отличаться от классической функции кроме трех новых необязательных аргументов:
# - start - с чего начинается вывод. По умолчанию пустая строка;
# - max_line - максимальная длин строки при выводе. Если строка превышает max_line, то вывод автоматически переносится на новую строку;
# - in_file - аргумент, определяющий будет ли записан вывод ещё и в файл.


def main():
    john = Contact('John', 'Smith', '+71234567809', 'Additional 1', 'Additional 2', telegram='@jhony',
                   email='jhony@smith.com')

    bob = Contact('Bob', 'Dilan', '+71234567808', 'Additional 1', 'Additional 2', favorite=True, telegram='@BobD',
                  email='Bob@dilan.com')

    bob2 = Contact('Bob', 'Dilan', '+71234567808', 'Additional 3', 'Additional 4', favorite=True, telegram='@BobD2',
                  email='Bob2@dilan.com')

    book = PhoneBook('Phones')
    book.add_contact(john)
    book.add_contact(bob)
    book.add_contact(bob2)

    book.print_favorites()

    book.print_contacts()

    book.delete_by_phone('+71234567809')
    book.print_contacts()

    book.search_by_name('Bob', 'Dilan')
    book.search_by_name('John', 'Smith')

    adv_print('test', 'kek', start='***', max_line=5, in_file=True)


if __name__ == '__main__':
    main()

