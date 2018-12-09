from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
post_collection = db["posts"]

new_post = {
    "title": "Học code để làm gì?",
    "author": "Hiển C4E24",
    "content": '''Học code để làm gì? Học code có kiếm được tiền không?
    Chắc là kiếm được thì mọi người mới học, nên cứ đi học đi nhé :)
    '''
}
post_collection.insert_one(new_post)
client.close()