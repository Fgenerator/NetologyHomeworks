import unittest
import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class TestTranslate(unittest.TestCase):

    def test_translate_it(self):
        lang = 'en'
        to_lang = 'ru'
        text = 'hello'

        params = {
            'key': API_KEY,
            'text': text,
            'lang': f'{lang}-{to_lang}',
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        self.assertEqual(json_['code'], 200)
        self.assertEqual(json_['text'][0], 'привет')

    def test_negative_translate_it_wrong_API(self):
        lang = 'en'
        to_lang = 'ru'
        text = 'hello'

        params = {
            'key': 'API_KEY',
            'text': text,
            'lang': f'{lang}-{to_lang}',
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        self.assertNotEqual(json_['code'], 200)
        self.assertEqual(json_['message'], 'API key is invalid')

    def test_negative_translate_it(self):

        response = requests.get(URL)
        json_ = response.json()
        self.assertNotEqual(json_['code'], 200)
        self.assertEqual(json_['message'], 'Invalid parameter: key')


if __name__ == '__main__':
    unittest.main()
