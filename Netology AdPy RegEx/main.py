from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


def get_contacts(filename):
    with open(filename, encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def upload_contacts(contacts, filename):
    with open(filename, "w", encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts)


def shake_names(contacts):
    for contact in contacts:
        if re.findall('\s', contact[0]):
            buffer = re.split('\s', contact[0])
            for part in buffer:
                contact[buffer.index(part)] = part

        if re.findall('\s', contact[1]):
            buffer = re.split('\s', contact[1])
            for part in buffer:
                contact[buffer.index(part) + 1] = part


def convert_phone(contacts):
    for contact in contacts:

        pattern = re.compile(r"(\+7|8)?\s*\((\d+)\)\s*(\d+)(\s*|\-?)(\d+)(\s*|\-?)(\d+)")
        text2 = pattern.sub(r"+7(\2)-\3-\5-\7", contact[5])
        print(text2)


def merge_duplicates(contacts):
    for contact_1 in contacts:
        for contact_2 in contacts:
            if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1] and contact_1 != contact_2:
                num = 0
                for field in contact_1:
                    num = contact_1.index(field, num)
                    if (contact_1[num] != contact_2[num]) and (contact_1[num] == ''):
                        contact_1[num] = contact_2[num]
                contacts.remove(contact_2)


# TODO 1: выполните пункты 1-3 ДЗ
# 1. поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# 2. привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер,
# ормат будет такой: +7(999)999-99-99 доб.9999;
# 3. объединить все дублирующиеся записи о человеке в одну.

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

def main():
    contacts_list = get_contacts("phonebook_raw.csv")
    shake_names(contacts_list)
    merge_duplicates(contacts_list)
    pprint(contacts_list)
    convert_phone(contacts_list)
    upload_contacts(contacts_list, "phonebook.csv")



if __name__ == '__main__':
    main()

