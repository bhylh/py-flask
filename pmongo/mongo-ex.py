from pymongo import MongoClient
import datetime
import pprint
url = 'mongodb://localhost:27017'
client = MongoClient(url)
dbName = 'test-databse'
currentDb = client[dbName]
collectionName = 'test-collection'
collection = currentDb[collectionName]
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
posts = currentDb.posts
## post_id = posts.insert_one(post).inserted_id
collections = currentDb.list_collection_names()

for cs in collections:
    print(cs)

first_post = posts.find_one()
pprint.pprint(first_post)

query_where = posts.find_one({"author": "Eliot"})
pprint.pprint(query_where)
