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
        #self.screen_name = screen_name

    def get_params(self) -> Dict:
        return {
            'access_token': TOKEN,
            'user_id': self.id,
            #'screen_name' = self.screen_name,
            'v': 5.89
        }

    def get_friends_ids(self) -> List[int]:
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        print('+')
        return response.json()['response']['items']

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
        #begin = time.monotonic()
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

    def get_group_info(self, data=None):
        if data:
            groups = data
        else:
            groups = self.get_unique_groups()
        params = self.get_params()
        result = []
        count = 0
        for group in groups:
            count += 1
            if count > 2:
                time.sleep(1)
                count = 0
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


def get_data_and_save(filename: str, user: User):
    with open('groups.txt', 'w') as outfile:
        json.dump(user.get_unique_groups(), outfile)


def load_data_from_file(filename: str):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_result(user, data=None):
    if data:
        groups = user.get_group_info(data)
    else:
        groups = user.get_group_info()
    result = []
    for group in groups:
        result.append({
            'id': group['id'],
            'name': group['name'],
            'count': group['members_count']
        })
    print(result)

    with open('result.txt', 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)


def main():
    with Timer() as timer:
        user = User('171691064')

        #get_data_and_save('groups.txt', user)

        #data = load_data_from_file('groups.txt')

        #get_result(user, data)
        get_result(user)


main()
