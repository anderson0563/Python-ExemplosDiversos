import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["futebol"]
mycol = mydb["times"]
mydict = { "time": "Barcelona", "atleta": "Messi" }

x = mycol.insert_one(mydict)