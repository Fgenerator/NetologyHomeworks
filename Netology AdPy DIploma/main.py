from packages.vkauth import VKAuth
from packages.users import User
import packages.mongo as mongo
from operator import itemgetter
import json
import time
import re


def prepare_users(users_from_vk, token, db):
    internal_users = []
    for vk_user in users_from_vk:
        internal_user = User(str(vk_user['id']), token)
        internal_user.closed = vk_user['is_closed']
        if not internal_user.closed and not mongo.is_user_in_db(internal_user, db):
            internal_users.append(internal_user)
    return internal_users


def prepare_photos(photos):
    internal_photos = []
    for photo in photos:
        internal_photos.append({
            'url': photo['sizes'][-1]['url'],
            'likes': photo['likes']['count'],
            'comments': photo['comments']['count']
        })
    return internal_photos


def sort_photos(internal_photos):
    # internal_photos = sorted(internal_photos, key=lambda k: (k['likes'], k['comments']))
    # internal_photos = sorted(internal_photos, key=itemgetter('likes', 'comments'))
    internal_photos.sort(key=itemgetter('likes', 'comments'))
    internal_photos.reverse()
    return internal_photos


def get_top_3_photos(sorted_internal_photos):
    return sorted_internal_photos[:3]


def prepare_data_to_json(internal_users):
    data = []
    for i, int_user in enumerate(internal_users[:10]):
        if i % 3 == 0:
            time.sleep(1)
        data.append({
            'page': int_user.page,
            'photos': get_top_3_photos(sort_photos(prepare_photos(int_user.get_photos())))
        })
    return data


def write_data_to_json(data_to_write, fname):
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(data_to_write, f, ensure_ascii=False, indent=4)

    print('Result written to data.json file')


def age_input():
    age_from, age_to = None, None
    while not age_from:
        age_from = re.escape(input('Введите нижнюю границу возраста для поиска (положительное число): '))
        if not (age_from.isdigit() and int(age_from) > 0):
            print('Некорректный возраст')
            age_from = None
    while not age_to:
        age_to = re.escape(input('Введите верхнюю границу возраста для поиска (положительное число, '
                                 'большее нижней границы поиска): '))
        if not (age_to.isdigit() and int(age_to) > int(age_from)):
            print('Некорректный возраст')
            age_to = None
    return age_from, age_to


def sex_input():
    sex = None
    while not sex:
        sex = re.escape(input('Введите пол (0 - любой, 1 - жен, 2 - муж): '))
        if sex.isdigit() and 0 <= int(sex) < 3:
            return sex
        else:
            print('Некорректный пол')
            sex = None


def city_input():
    city = None
    while not city:
        city = re.escape(input('Введите город поиска: '))
        if city.isalnum():
            return city
        else:
            print('Некорректный город')
            city = None


def status_input():
    status = None
    while not status:
        print('Введите семейное положение.')
        print('1 — не женат (не замужем);\n2 — встречается;\n3 — помолвлен(-а);\n4 — женат (замужем);\n'
              '5 — всё сложно;\n6 — в активном поиске;\n7 — влюблен(-а);\n8 — в гражданском браке.')
        status = re.escape(input('> '))
        if status.isdigit() and 0 < int(status) < 9:
            return status
        else:
            print('Некорректное семейное положение')
            status = None


def authorize():
    vk_auth = VKAuth(['photos', 'friends'], '7566412', '5.89')

    vk_auth.auth()

    print('Authorized successfully\n')

    access_token = vk_auth.get_token()
    user_id = vk_auth.get_user_id()

    return access_token, user_id


def start(user, token, db):
    print('VKinder')

    while True:
        print('Список команд: ')
        print('1 - начать новый поиск;')
        print('0 - выход.')

        user_input = input('> ')

        if user_input == '1':
            age_from, age_to = age_input()
            sex = sex_input()
            city = city_input()
            status = status_input()

            users = prepare_users(user.search_users(age_from, age_to, sex, city, status), token, db)

            data = prepare_data_to_json(users)

            write_data_to_json(data, 'data.json')

            mongo.write_data(data, db)
        elif user_input == '0':
            break
        else:
            print('Такой команды нет')


def main():
    access_token, user_id = authorize()

    vk_users_db = mongo.prepare_db()

    user = User(user_id, access_token)

    start(user, access_token, vk_users_db)


if __name__ == '__main__':
    main()
