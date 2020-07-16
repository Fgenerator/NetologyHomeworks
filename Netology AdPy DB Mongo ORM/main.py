import csv
import re

from pymongo import MongoClient


def prepare_db():
    client = MongoClient()
    db = client['netology']
    return db


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        artists_collection = db.artists
        artists = []
        for row in reader:
            artists.append({
                'name': row['Исполнитель'],
                'cost': row['Цена'],
                'place': row['Место'],
                'date': row['Дата']
            })
        artists_collection.insert_many(artists)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    print(list(db.artists.find().sort([('cost', 1)]))[0])
    print(list(db.artists.find().sort([('cost', 1)])))


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    # 'укажите регулярное выражение для поиска. ' \
    # 'Обратите внимание, что в строке могут быть специальные символы, их нужно экранировать'
    regex = re.compile('/*'+name+'/*')
    print(list(db.artists.find({'name': {'$regex': regex}}).sort([('cost', -1)])))


if __name__ == '__main__':
    netology_db = prepare_db()
    read_data('artists.csv', netology_db)
    print(list(netology_db.artists.find()))
    find_cheapest(netology_db)
    find_by_name('1', netology_db)

    netology_db.artists.delete_many({})


