import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
REQUEST_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
OAUTH_TOKEN = 'OAuth '


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


def upload_to_yadisk(filename):
    """
        https://cloud-api.yandex.net/v1/disk/resources/upload
        ? path=<путь, по которому следует загрузить файл>
        & [overwrite=<признак перезаписи>]
        & [fields=<свойства, которые нужно включить в ответ>]
        :param filename:
        """
    auth_headers = {
        'Accept': 'application/json',
        'Authorization': OAUTH_TOKEN
    }

    #auth_response = requests.get(AUTH_URL, headers=auth_headers)
    #auth_json = auth_response.json()
    #print(auth_json)

    request_params = {
        'path': filename,
        'overwrite': 'true',
        'fields': ''
    }
    upload_url = ''

    try:
        response = requests.get(REQUEST_URL, params=request_params, headers=auth_headers)
        json_ = response.json()

        upload_url = json_['href']
    except KeyError:
        print('Something wrong with upload URL request.')

    try:
        upload_response = requests.put(upload_url, data=open(filename, 'rb'))
    except Exception:
        print('Something wrong with uploading.')
    else:
        if upload_response.status_code == 201:
            print(f'File {filename} successfully uploaded to Yandex.Disk.')


if __name__ == '__main__':
    translate_it('DE.txt', 'Translated DE-RU.txt', 'de')
    translate_it('ES.txt', 'Translated ES-RU.txt', 'es')
    translate_it('FR.txt', 'Translated FR-RU.txt', 'fr')
    translate_it('DE.txt', 'Translated DE-EN.txt', 'de', 'en')

    upload_to_yadisk('Translated DE-RU.txt')
    upload_to_yadisk('Translated ES-RU.txt')
    upload_to_yadisk('Translated FR-RU.txt')
    upload_to_yadisk('Translated DE-EN.txt')


