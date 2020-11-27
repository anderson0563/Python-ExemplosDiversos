import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["futebol"]
mycol = mydb["times"]

mydoc = mycol.find()

for x in mydoc:
  print(x)

