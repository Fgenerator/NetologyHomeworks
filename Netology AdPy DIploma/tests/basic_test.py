from packages.vkauth import VKAuth
from packages.users import User
import packages.mongo as mongo

from unittest.mock import patch

import pytest

import main


def auth():
    with patch('builtins.input', side_effect=['login']):
        with patch('getpass.getpass', side_effect=['pass']):
            access_token, user_id = main.authorize()
    return access_token, user_id


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




