from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

client = MongoClient(MONGODB_URL, tlsCAFile=certifi.where())

db = client["Alpha_Agent_db"]
users_collection = db["users"]
history_collection = db["history"]