from vkauth import VKAuth
from users import User

vk_auth = VKAuth(['photos', 'friends'], '7556238', '5.89')

vk_auth.auth()

access_token = vk_auth.get_token()
user_id = vk_auth.get_user_id()

user = User(user_id, access_token)

print(user.get_params())

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