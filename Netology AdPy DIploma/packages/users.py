import requests
import sys
import time
from typing import List


class User:
    def __init__(self, call: str, token: str) -> None:
        self.token = token
        if call.isdigit():
            self.id = call
        else:
            params = {
                'access_token': self.token,
                'v': 5.89,
                'user_ids': call
            }
            try:
                response = requests.get(
                    'https://api.vk.com/method/users.get',
                    params
                )
            except Exception as e:
                print('Something wrong with user id request')
            try:
                self.id = response.json()['response'][0]['id']
            except Exception as e:
                sys.exit('Bad response with user ID')

    def get_params(self) -> dict:
        try:
            return {
                'access_token': self.token,
                'user_id': self.id,
                'v': 5.89
            }
        except AttributeError as e:
            print('Bad params attribute')

    def search_users(self, age_from, age_to, sex, hometown, marriage):
            ...
