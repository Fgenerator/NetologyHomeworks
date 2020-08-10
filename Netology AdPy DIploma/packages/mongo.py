from pymongo import MongoClient


def prepare_db():
    client = MongoClient()
    db = client['vk_users']
    return db


def write_data(data, db):
    vk_users_collection = db.users
    vk_users_collection.insert_many(data)


def get_pages_from_collection(db):
    pages = []
    for user in list(db.users.find()):
        pages.append(user['page'])
    return pages


def is_user_in_db(internal_user, db):
    return internal_user.page in get_pages_from_collection(db)



