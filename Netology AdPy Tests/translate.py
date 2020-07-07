import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(input_file, output_file, lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param input_file:
    :param output_file:
    :param lang:
    :param to_lang:
    """
    with open(input_file, encoding='utf8') as ifile:
        text = ifile.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{lang}-{to_lang}',
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(output_file, 'w', encoding='utf8') as ofile:
        ofile.write(''.join(json_['text']))
    print(f'File {output_file} created.')


if __name__ == '__main__':
    translate_it('DE.txt', 'Translated DE-RU.txt', 'de')
    translate_it('ES.txt', 'Translated ES-RU.txt', 'es')
    translate_it('FR.txt', 'Translated FR-RU.txt', 'fr')
    translate_it('DE.txt', 'Translated DE-EN.txt', 'de', 'en')