from pymongo import MongoClient
from config import *
import sys
import json

def delete(query_filter):
	client = MongoClient(CONNECTION_STRING)
	database = client[DATABASE]
	collection = database[COLLECTION]
	result = collection.delete_many(query_filter)
	print(result.raw_result)
	
	
if __name__ == '__main__':
    delete(sys.argv[1])
    
