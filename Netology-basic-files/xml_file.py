import xml.etree.ElementTree as ET
from words_funcs import *


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


def main():
    tree = get_tree_from_xml('newsafr.xml')
    items = get_items_from_tree(tree, 'channel/item')
    texts = get_texts_from_items(items, 'description')
    words = get_words_from_texts(texts)
    count_top(words, 10)


main()
