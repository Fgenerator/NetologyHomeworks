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

    def get_country_id(self):
        params = self.get_params()

        try:
            response = requests.get(
                'https://api.vk.com/method/database.getCountries',
                params
            )
        except Exception as e:
            print('Something wrong with get country request')
        try:
            return response.json()['response']['items'][0]['id']
        except KeyError as e:
            print('Bad get country response')

    def get_city_id(self, city: str):
        params = self.get_params()
        if len(city) > 15:
            city = city[0:15]
        params['q'] = city
        params['country_id'] = self.get_country_id()
        params['count'] = 1

        try:
            response = requests.get(
                'https://api.vk.com/method/database.getCities',
                params
            )
        except Exception as e:
            print('Something wrong with get cities request')
        try:
            return response.json()['response']['items'][0]['id']
        except KeyError as e:
            print('Bad get cities response')

    def search_users(self, age_from: int, age_to: int, sex: int, city: str, status: int):
        params = self.get_params()
        params['age_from'] = age_from
        params['age_to'] = age_to
        params['sex'] = sex
        params['city'] = self.get_city_id(city)
        params['status'] = status
        params['count'] = 100

        try:
            response = requests.get(
                'https://api.vk.com/method/users.search',
                params
            )
        except Exception as e:
            print('Something wrong with users search request')
        try:
            return response.json()['response']['items']
        except KeyError as e:
            print('Bad get users search response')