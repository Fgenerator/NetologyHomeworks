from pprint import pprint
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
                contact[buffer.index(part)+1] = part


def convert_phones(contacts):
    for contact in contacts:
        regex = r'(\+7|8)\s?\(?(\d+)\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})'
        pattern = re.compile(regex)
        contact[5] = pattern.sub(r'+7(\2)-\3-\5', contact[5])

        regex = r'(\(?)([д][о][б]\.?)\s?(\d+)(\)?)'
        pattern = re.compile(regex)
        contact[5] = pattern.sub(r'\2\3', contact[5])


def merge_duplicates(contacts):
    for contact_1 in contacts:
        for contact_2 in contacts:
            if contact_1[0] == contact_2[0] \
                    and contact_1[1] == contact_2[1] \
                    and contact_1 != contact_2:
                num = 0
                for field in contact_1:
                    num = contact_1.index(field, num)
                    if (contact_1[num] != contact_2[num]) \
                            and (contact_1[num] == ''):
                        contact_1[num] = contact_2[num]
                contacts.remove(contact_2)


# TODO 1: выполните пункты 1-3 ДЗ
# 1. поместить Фамилию, Имя и Отчество человека в поля
# lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО,
# а может быть сразу правильно: Ф+И+О;
# 2. привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер,
# формат будет такой: +7(999)999-99-99 доб.9999;
# 3. объединить все дублирующиеся записи о человеке в одну.

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

def main():
    contacts_list = get_contacts("phonebook_raw.csv")
    shake_names(contacts_list)
    merge_duplicates(contacts_list)
    convert_phones(contacts_list)
    pprint(contacts_list)
    upload_contacts(contacts_list, "phonebook.csv")


if __name__ == '__main__':
    main()
