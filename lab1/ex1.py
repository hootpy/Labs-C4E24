from pymongo import MongoClient
uri = "mongodb://admin:abc123@ds050559.mlab.com:50559/c4e24-lab1"
client = MongoClient(uri)

db = client.get_database()

account = db["account"]
for i in account.find():
    print(i)

# new_account = {
#     "username": "vn123",
#     "email": "vn123@gmail.com",
#     "phone": "0987654321",
#     "password": "vn123"
# }

# account.insert_one(new_account)
client.close()