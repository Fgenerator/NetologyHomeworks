import json
from collections import Counter
from pprint import pprint


def open_json(file):
    with open(file, encoding='utf-8') as f:
        return json.load(f)


def get_words(data):
    words = []
    for item in data['rss']['channel']['items']:
        text = item['description'].split()
        for word in text:
            if len(word) > 6:
                words.append(word)
    return words


def main():
    data = open_json('newsafr.json')
    words = get_words(data)
    print(Counter(words).most_common(10))


main()

