import os
from dotenv import load_dotenv
from pymongo import MongoClient

if not os.getenv("MONGO_URI"):
    load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

# connection to mongodb
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
collection_name = db[MONGO_COLLECTION_NAME]
