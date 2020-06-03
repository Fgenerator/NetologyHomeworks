from pprint import pprint
from urllib.parse import urlencode
import requests
import time
import json
from typing import List
from typing import Dict

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

class User:
    def __init__(self, id: str) -> None:
        self.id = id

    def __and__(self, other):
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
        print('+')
        return response.json()['response']['items']

    def get_friends_info(self) -> List[str]:
        params = self.get_params()
        params['user_ids'] = str(self.get_friends_ids())
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        return response.json()['response']

    def get_groups(self) -> Dict:
        params = self.get_params()
        params['extended'] = 1
        print('*')
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        groups = []
        try:
            print(response.json()['response']['items'])
            for group in response.json()['response']['items']:
                groups.extend(group['id'])
            return groups
        except KeyError as e:
            id = response.json()['error']['request_params'][0]['value']
            error = response.json()['error']['error_msg']
            print(id, error)

    def get_friends_groups(self):
        friends = self.get_friends_ids()
        groups = []
        count = 0
        for friend in friends:
            count += 1
            if count > 2:
                time.sleep(0.5)
                count = 0
            groups.extend(User(friend).get_groups())
        return groups
"""
Получить список групп пользователя
Получить список друзей
Получить списки групп друзей

"""
def main():
    user = User('11433647')
    user2 = User('174467064')
    # print(user.get_friends_ids())
    # print(user2.get_friends_ids())

    user_groups = user.get_groups()
    print(set(user_groups))

    user_friends_groups = user.get_friends_groups()
    print(set(user_friends_groups))



    #with open('groups.txt', 'w') as outfile:
       #json.dump(user.get_friends_groups(), outfile)


main()
