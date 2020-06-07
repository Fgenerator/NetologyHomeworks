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
    def __init__(self, call: str) -> None:
        if call.isdigit():
            self.id = call
        else:
            params ={
                'access_token': TOKEN,
                'v': 5.89,
                'user_ids': call
            }
            response = requests.get(
                'https://api.vk.com/method/users.get',
                params
            )
            self.id = response.json()['response'][0]['id']

    def get_params(self) -> Dict:
        return {
            'access_token': TOKEN,
            'user_id': self.id,
            'v': 5.89
        }

    def get_friends_ids(self) -> List[int]:
        params = self.get_params()
        print('Friends request')
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        return response.json()['response']['items']

    def get_groups(self) -> Dict:
        params = self.get_params()
        params['extended'] = 1
        print('Groups request')
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
        for i, friend in enumerate(friends):
            if i % 3 == 0:
                time.sleep(1)
            try:
                groups.extend(User(str(friend)).get_groups())
            except TypeError:
                ...
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
        for i, group in enumerate(groups):
            if i % 3 == 0:
                time.sleep(1)
            params['group_id'] = group
            params['fields'] = 'members_count'
            print('Groups info request')
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params
            )
            result.append(response.json()['response'][0])
        return result


def get_data_and_save(filename: str, user: User):
    with open(filename, 'w') as outfile:
        json.dump(user.get_unique_groups(), outfile)


def load_data_from_file(filename: str):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_result(user, data=None):
    groups = user.get_group_info(data)
    result = [{
            'id': group['id'],
            'name': group['name'],
            'count': group['members_count']
        } for group in groups]
    print(result)

    with open('result.txt', 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)


def main():
    with Timer() as timer:
        # user = User('171691064')
        user = User('eshmargunov')

        # get_data_and_save('groups.txt', user)

        # data = load_data_from_file('groups.txt')

        # get_result(user, data)

        get_result(user)


main()
