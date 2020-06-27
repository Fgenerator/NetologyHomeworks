

class Contact:
    def __init__(self,
                 first_name: str, second_name: str, phone: str,
                 favorite=False,
                 *args, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.favorite = favorite
        self.addition_args = [arg for arg in args]
        self.addition_kwargs = kwargs

    def __str__(self):
        first_name_str = f'First name: {self.first_name}\n'
        second_name_str = f'Second name: {self.second_name}\n'
        phone_str = f'Phone name: {self.phone}\n'
        is_favorite_str = f'Favorite: {self.is_favorite()}\n'
        additional_str = f'{self.type_additional()}'
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

# ```
# Имя: Jhon
# Фамилия: Smith
# Телефон: +71234567809
# В избранных: нет
# Дополнительная информация:
# 	 telegram : @jhony
# 	 email : jhony@smith.com
# ```


class PhoneBook:
    def __init__(self, name: str):
        self.name = name
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def print_contacts(self):
        for contact in self.contacts:
            print(contact)

    def delete_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)

    def print_favorites(self):
        for contact in self.contacts:
            if contact.favorite:
                print(contact)

    def search_by_name(self, first_name, second_name):
        sign = 1
        for contact in self.contacts:
            if contact.first_name == first_name and contact.second_name == second_name:
                print(contact)
                sign = 0
        if sign:
            print(f'{first_name} {second_name} not in phonebook {self.name}')


# - Название телефонной книги - обязательное поле;
# - Телефонная книга должна работать с классами Contact.
#
# Методы:
# - Вывод контактов из телефонной книги;
# - Добавление нового контакта;
# - Удаление контакта по номеру телефона;
# - Поиск всех избранных номеров;
# - Поиск контакта по имени и фамилии.


def main():
    john = Contact('John', 'Smith', '+71234567809', False, 'Additional 1', 'Additional 2', telegram='@jhony',
                   email='jhony@smith.com')

    bob = Contact('Bob', 'Dilan', '+71234567808', True, 'Additional 1', 'Additional 2', telegram='@BobD',
                  email='Bob@dilan.com')

    book = PhoneBook('Phones')
    book.add_contact(john)
    book.add_contact(bob)

    book.print_favorites()

    book.print_contacts()

    book.delete_by_phone('+71234567808')
    book.print_contacts()

    book.search_by_name('Bob', 'Dilan')
    book.search_by_name('John', 'Smith')


if __name__ == '__main__':
    main()
