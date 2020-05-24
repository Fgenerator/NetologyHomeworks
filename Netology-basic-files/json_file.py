import json
from pprint import pprint


def open_json(file):
    with open(file, encoding='utf-8') as f:
        return json.load(f)


def get_words(data):
    words = []
    for item in data['rss']['channel']['items']:
        text = item['description'].split(' ')
        for word in text:
            if len(word) > 6:
                words.append(word)
    return words


def count_words(words):
    top_words = {}
    for word in words:
        if word in top_words:
            top_words[word] += 1
        else:
            top_words[word] = 1
    return top_words


def sort_words_by_count(words_with_counts):
    words_list = sorted(words_with_counts.items(), reverse=True, key=lambda item: item[1])
    names = [name for name, count in words_list]
    return names


def main():
    data = open_json('newsafr.json')
    words = get_words(data)
    words_with_counts = count_words(words)
    sorted_words = sort_words_by_count(words_with_counts)
    pprint(sorted_words[0:10])


main()
