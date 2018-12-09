import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
customer = db["customers"]

events_count = 0
ads_count = 0
wom_count = 0

for i in customer.find():
    if i["ref"] == "events":
        events_count += 1
    elif i["ref"] == "ads":
        ads_count += 1
    else:
        wom_count += 1

print("The number of customers from events: ",events_count)
print("The number of customers from word of mouth: ",wom_count)
print("The number of customers from advertisements: ",ads_count)

client.close()
ref = [events_count,wom_count,ads_count]
label = ["Events", "Word of mouth","Advertisements"]

pyplot.pie(ref,labels=label,shadow=True, explode=(0 ,0 ,0.1),autopct='%1.1f%%',startangle=90)
pyplot.axis("equal")
pyplot.title("Percentage in reference")
pyplot.show()
