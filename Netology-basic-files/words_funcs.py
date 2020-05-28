from collections import Counter


def get_words_from_texts(texts):
    words = []
    for text in texts:
        text = text.split()
        for word in text:
            if len(word) > 6:
                words.append(word.lower())
    return words


def count_top(words, number):
    top = Counter(words).most_common(number)
    for word, count in top:
        print(f'{word} - {count}')