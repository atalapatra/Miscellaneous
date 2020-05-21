import pandas as pd
from pymongo import MongoClient
import pprint
import json

# Print all docs in collection
def print_all_in_collection(collection):
    cursor = collection.find()
    for doc in cursor:
        print(doc)

if __name__ == "__main__":
    # Identify connection information
    connections = json.load(open('C:/Users/amitt/OneDrive/Code/2020-05-08 Python with MongoDB/connection.json'))
    uri = connections['MongoDB Atlas']['mflix URI']

    # Connect to database
    client = MongoClient(uri)

    # View database info
    client.server_info()

    # View databases
    client.database_names()

    # Connect to a database and view collections
    db = client.pubs
    db.collection_names()

    # Bring collections into Python
    british_pubs = db['british_pubs']
    welsh_pubs = db['welsh_pubs']

    # View a document
    pprint.pprint(british_pubs.find_one())

    # Save document in Python
    document = british_pubs.find_one()

    # Save collections as dfs
    british_pubs_df =  pd.DataFrame(list(british_pubs.find()))
    welsh_pubs_df =  pd.DataFrame(list(welsh_pubs.find()))

    # Count pubs by local authority
    brit_pubs_by_local = british_pubs_df[['local_authority', 'fsa_id', 'name']].groupby(['local_authority']).count()