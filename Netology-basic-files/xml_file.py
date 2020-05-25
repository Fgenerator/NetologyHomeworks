import xml.etree.ElementTree as ET
from collections import Counter
from pprint import pprint


def get_tree_from_xml(file):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file, parser)
    return tree


def get_items_from_tree(tree, path):
    root = tree.getroot()
    items = root.findall(path)
    return items


def get_texts_from_items(items, field):
    texts = []
    for item in items:
        texts.append(item.find(field).text)
    return texts


def get_words_from_texts(texts):
    words = []
    for text in texts:
        text = text.split()
        for word in text:
            if len(word) > 6:
                words.append(word)
    return words


def main():
    tree = get_tree_from_xml('newsafr.xml')
    items = get_items_from_tree(tree, 'channel/item')
    texts = get_texts_from_items(items, 'description')
    words = get_words_from_texts(texts)
    top = Counter(words).most_common(10)
    for word, count in top:
        print(f'{word} - {count}')


main()



