from packages.vkauth import VKAuth
from packages.users import User
import packages.mongo as mongo

from unittest.mock import patch

import pytest

import main


def auth():
    with patch('builtins.input', return_value='login'):
        with patch('getpass.getpass', return_value='password'):
            access_token, user_id = main.authorize()
    return access_token, user_id


def create_user():
    access_token, user_id = auth()
    user = User(user_id, access_token)
    return user


def search_users():
    user = create_user()
    users = user.search_users(20, 25, 1, 'Москва', 6)
    return users


def test_auth():
    access_token, user_id = auth()

    assert access_token.isalnum() and len(access_token) == 85 and user_id.isdigit()


def test_prepare_db():
    vk_users_db = mongo.prepare_db()

    assert vk_users_db.Database.Mongoclient.connect


def test_user_creation():
    access_token, user_id = auth()

    user = User(user_id, access_token)

    assert user.id == user_id


def test_search_users():
    user = create_user()
    users = user.search_users(20, 25, 1, 'Москва', 6)

    assert users[0]['id']


def test_negative_search_users():
    user = create_user()
    users = user.search_users(100, 25, 1, 'Москва', 6)

    assert not users


def test_prepare_users():
    users = search_users()
    users = main.prepare_users(users)

    for user in users:
        assert user.id