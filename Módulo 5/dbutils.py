from pymongo import MongoClient

MONGO_URI="mongodb+srv://admin:admin@cluster0-skqfo.mongodb.net/test"

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection

def db_insert_user(collection, user):
    return collection.insert_one(user)

def db_find_all(collection, query={}):
        return collection.find(query)

if __name__ == '__main__':
    print("MongoClient imported successfully!")

#database = client['mi_app']

#users = database['users']

#usuario_demo = {
#          "user": "Fernanda Winkel",
#          "email": "fernandacww@homail.com"
#}
#users.insert_one(usuario_demo)
