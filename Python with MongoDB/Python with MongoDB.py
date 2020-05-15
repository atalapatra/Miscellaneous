import pymongo
from pymongo import MongoClient
import pprint
import json

connections = json.load(open('C:/Users/amitt/OneDrive/Code/2020-05-08 Python with MongoDB/connection.json'))
uri = connections['MongoDB Atlas']['mflix URI']

client = MongoClient(uri)

db = client.aggregations





connection_data = json.dumps(connections, indent=4)

client = MongoClient(uri)



client.database_names()

db = client.aggregations

db.list_collection_names()

air_alliances = db.air_alliances

pprint.pprint(air_alliances.find_one())
