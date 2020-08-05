from pymongo import MongoClient


def prepare_db():
    client = MongoClient()
    db = client['netology']
    return db


def read_data(data, db):
        for user in data:
            row['Дата'] = f'{row["Дата"]}.{datetime.now().year}'
            date = datetime.strptime(row['Дата'], '%d.%m.%Y')
            artists.append({
                'name': row['Исполнитель'],
                'cost': int(row['Цена']),
                'place': row['Место'],
                'date': date
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
    name = re.escape(name)
    regex = re.compile('/*'+name+'/*')
    print(list(db.artists.find({'name': {'$regex': regex}}).sort([('cost', -1)])))


def sort_by_date(db):
    print(list(db.artists.find().sort([('date', 1)])))


if __name__ == '__main__':
    netology_db = prepare_db()
    read_data('artists.csv', netology_db)
    print(list(netology_db.artists.find()))
    find_cheapest(netology_db)
    find_by_name('[a-Z]*', netology_db)
    find_by_name('1', netology_db)
    sort_by_date(netology_db)

    netology_db.artists.delete_many({})


