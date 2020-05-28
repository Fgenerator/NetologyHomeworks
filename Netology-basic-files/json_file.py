import json
from words_funcs import *


def open_json(file):
    with open(file, encoding='utf-8') as f:
        return json.load(f)


def get_items_from_data(data):
    items = []
    for item in data['rss']['channel']['items']:
        items.append(item)
    return items


def get_texts_from_items(items, field):
    texts = []
    for item in items:
        texts.append(item[field])
    return texts


def main():
    data = open_json('newsafr.json')
    items = get_items_from_data(data)
    texts = get_texts_from_items(items, 'description')
    words = get_words_from_texts(texts)
    count_top(words, 10)


main()
