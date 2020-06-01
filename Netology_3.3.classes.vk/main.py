from pprint import pprint
from urllib.parse import urlencode
import requests
from typing import List
from typing import Dict

OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMs = {
    'client_id': 7490544,
    'display': 'page',
    'scope': '',
    'response_type': 'token',
    'v': 5.89
}
TOKEN = ''


class User:
    def __init__(self, id: str) -> None:
        self.id = id

    def __and__(self, other) -> List[str]:
        friends_one = set(self.get_friends_ids())
        friends_two = set(other.get_friends_ids())
        mutual = friends_one & friends_two
        users = []
        for friend in mutual:
            users.append(User(friend))
        return users

    def __str__(self) -> str:
        return f'vk.com/id{self.id}'

    def get_params(self) -> Dict:
        return {
            'access_token': TOKEN,
            'user_id': self.id,
            'v': 5.89
        }

    def set_status(self, text: str) -> str:
        params = self.get_params()
        params['text'] = text
        response = requests.get(
            'https://api.vk.com/method/status.set',
            params
        )
        return response.json()['response']

    def get_status(self) -> str:
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/status.get',
            params
        )
        return response.json()['response']['text']

    def get_friends_ids(self) -> List[int]:
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        return response.json()['response']['items']

    def get_friends_info(self) -> List[str]:
        params = self.get_params()
        params['user_ids'] = str(self.get_friends_ids())
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        return response.json()['response']


def main():
    print('?'.join(
        (OAUTH_URL, urlencode(OAUTH_PARAMs))
    ))

    user = User('11433647')
    user2 = User('174467064')
    print(user.get_friends_ids())
    print(user2.get_friends_ids())

    mutual = user & user2
    for user in mutual:
        print(user)


main()
