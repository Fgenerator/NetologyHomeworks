import json
import requests
import hashlib
import datetime
from typing import List

URL = 'https://en.wikipedia.org/w/api.php'
PARAMS = {
    "action": "query",
    "format": "json"
}


def open_json(file: str) -> any:
    with open(file, encoding='utf-8') as f:
        return json.load(f)


def get_country_list(data: any) -> List:
    country_list = [item['name']['common'] for item in data]
    return country_list


class CountryIterator:
    def __init__(self, country_list):
        self.countries_iterator = iter(country_list)
        self.session = requests.Session()

    def __iter__(self):
        return self

    def __next__(self):
        country = next(self.countries_iterator)
        id = self.get_page_id(country)
        url = self.get_page_url(id)
        return country, url

    def get_page_id(self, country):
        params = PARAMS
        params["srsearch"] = country
        params["list"] = "search"

        try:
            result = self.session.get(url=URL, params=PARAMS)
        except Exception:
            print('Wrong page id request')

        try:
            return result.json()['query']['search'][0]['pageid']
        except Exception:
            print('Wrong page id response')

    def get_page_url(self, id):
        params = PARAMS
        params['pageids'] = id
        params['prop'] = 'info'
        params['inprop'] = 'url'

        try:
            result = self.session.get(url=URL, params=PARAMS)
        except Exception:
            print('Wrong page url response')

        try:
            return result.json()['query']['pages'][str(id)]['fullurl']
        except Exception:
            print('Wrong page url response')


def param_decor(log_path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(log_path, 'w', encoding='utf8') as log_file:
                now = datetime.datetime.now()
                log_file.write(f'{now}: \'{old_function.__name__}\' function\nwith args: {args}\nand kwargs: {kwargs}\nResult: {result}')
            return result
        return new_function
    return decorator


@param_decor('log.txt')
def perform_file(country_list, filename):
    with open(filename, 'w', encoding='utf8') as ofile:
        for country, url in CountryIterator(country_list):
            ofile.write(f'{country} -- {url}\n')
            print(f'{country} with url: {url} added to file')
    return True


def hash_from_file_generator(filename):
    with open(filename, 'r', encoding='utf8') as ifile:
        line = ifile.readline()
        while line:
            line = ifile.readline()
            yield hashlib.sha256(line.encode()).hexdigest()


def main():
    data = open_json('countries.json')
    countries = get_country_list(data)
    perform_file(countries, 'result.txt')

    for hash in hash_from_file_generator('result.txt'):
        print(hash)


if __name__ == '__main__':
    main()


