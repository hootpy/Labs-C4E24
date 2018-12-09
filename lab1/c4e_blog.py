from pymongo import MongoClient

#1. Connect to data base server
uri = "mongodb://admin:abc123@ds050559.mlab.com:50559/c4e24-lab1"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
post_collection = db["posts"]

# for post in post_collection.find():
#     print(post)

# #4. Create document
# new_document = {
#     'title': 'Hom nay Vietnam thang',
#     'post': 'Minh van o nha code =))) hihi',
# }

# #5. Add document into collection
# post_collection.insert_one(new_document)

#6. Close connection
client.close()