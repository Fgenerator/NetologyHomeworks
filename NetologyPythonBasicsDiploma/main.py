from pprint import pprint
from urllib.parse import urlencode
import requests
import time
import json
from typing import List
from typing import Dict

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


class Timer:
    def __init__(self):
        self.working_time = 0

    def __enter__(self):
        self.begin = time.monotonic()
        print(f'{self.begin}: начало работы.\n')

    def calculate_time(self):
        self.working_time = self.end - self.begin
        return self.working_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'error: {exc_val}')
        self.end = time.monotonic()
        print(f'{self.end}: конец работы.')
        print(f'{self.calculate_time()}: общее время работы.')


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
            #print(response.json()['response']['items'])
            for group in response.json()['response']['items']:
                groups.append(group['id'])
            return groups
        except KeyError as e:
            id = response.json()['error']['request_params'][0]['value']
            error = response.json()['error']['error_msg']
            print(id, error)

    def get_friends_groups(self):
        friends = self.get_friends_ids()
        groups = []
        count = 0
        begin = time.monotonic()
        for friend in friends:
            count += 1
            if count > 2:  # and end - begin >= 1:
                time.sleep(1)
                count = 0
                #begin = time.monotonic()
            try:
                groups.extend(User(friend).get_groups())
            except TypeError:
                ...
            #end = time.monotonic()
        return groups

    def get_unique_groups(self):
        user_groups = self.get_groups()
        friends_groups = self.get_friends_groups()
        return list(set(user_groups) - set(friends_groups))

    def get_group_info(self, data):
        # groups = self.get_unique_groups()
        groups = data
        params = self.get_params()
        result = []
        for group in groups:
            params['group_id'] = group
            params['fields'] = 'members_count'
            print('*')
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params
            )
            result.append(response.json()['response'][0])
        return result

"""
Получить список групп пользователя
Получить список друзей
Получить списки групп друзей

"""


def main():
    with Timer() as timer:
        user = User('11433647')
        user2 = User('174467064')
        user3 = User('171691064')

        #result = user3.get_unique_groups()
        #print(type(result))
        #print(result)

        #user3.get_group_info()

        with open('groups.txt', encoding='utf-8') as f:
            data = json.load(f)

        groups = user3.get_group_info(data)
        result = []
        for group in groups:
            result.append({
                'id': group['id'],
                'name': group['name'],
                'count': group['members_count']
            })
        print(result)

        with open('result.txt', 'w', encoding='utf-8') as outfile:
            json.dump(result, outfile)

        #print(data)
        #user_groups = user3.get_groups()
        #friends_groups = data
        #data = set(user_groups) - set(friends_groups)
        #user3.get_group_info(list(data))

        #with open('groups.txt', 'w') as outfile:
            #json.dump(user3.get_unique_groups(), outfile)


main()
