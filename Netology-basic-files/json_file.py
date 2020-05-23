import json
from pprint import pprint

with open('newsafr.json', encoding='utf-8') as f:
    data = json.load(f)
    pprint(data)