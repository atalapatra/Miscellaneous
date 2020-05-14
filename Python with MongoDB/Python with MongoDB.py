import pymongo
from pymongo import MongoClient
import pprint

connections = ('C:/Users/amitt/OneDrive/Code/2020-05-08 Python with MongoDB/connection.json')


client = MongoClient(uri)



client.database_names()

db = client.aggregations

db.list_collection_names()

air_alliances = db.air_alliances

pprint.pprint(air_alliances.find_one())
