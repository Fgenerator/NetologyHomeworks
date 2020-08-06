from vkauth import VKAuth
from users import User
import db
from pprint import pprint
from operator import itemgetter
import json
import time


def prepare_users(users_from_vk, token):
    internal_users = []
    for vk_user in users_from_vk:
        internal_user = User(str(vk_user['id']), token)
        internal_user.closed = vk_user['is_closed']
        if not internal_user.closed:
            internal_users.append(internal_user)
    # print('internal users prepared')
    return internal_users


def prepare_photos(photos):
    internal_photos = []
    for photo in photos:
        internal_photos.append({
            'url': photo['sizes'][-1]['url'],
            'likes': photo['likes']['count'],
            'comments': photo['comments']['count']
        })
    # print('internal photos prepared')
    return internal_photos


def sort_photos(internal_photos):
    # internal_photos = sorted(internal_photos, key=lambda k: (k['likes'], k['comments']))
    # internal_photos = sorted(internal_photos, key=itemgetter('likes', 'comments'))
    internal_photos.sort(key=itemgetter('likes', 'comments'))
    internal_photos.reverse()
    # print('internal photos sorted')
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
    print('data prepared to json')
    return data


def write_data_to_json(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


vk_auth = VKAuth(['photos', 'friends'], '7556238', '5.89')

vk_auth.auth()

access_token = vk_auth.get_token()
user_id = vk_auth.get_user_id()

user = User(user_id, access_token)

users = prepare_users(user.search_users(20, 25, 1, 'Тюмень', 6), access_token)

data = prepare_data_to_json(users)

write_data_to_json(data)

vk_users_db = db.prepare_db()

db.read_data(data, vk_users_db)

pprint(list(vk_users_db.users.find()))

pprint(len(list(vk_users_db.users.find())))

# vk_users_db.users.delete_many({})

"""

Поиск людей
    Ввод информации
        Если информация в профиле не указана, то спросить для поиска

    Искать людей, подходящих под условия, на основании информации о пользователе из VK:
        - возраст,
        - пол,
        - город,
        - семейное положение

Вывод в JSON
    JSON-файл с 10 объектами, где у каждого объекта перечислены топ-3 фотографии
    и ссылка на аккаунт.

БД
    Таблица с пользователями сервиса
    Таблица с пользователями вк

Тесты
    pytest

"""