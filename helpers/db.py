"""
DB-File
"""
from pymongo import MongoClient
from bson.objectid import ObjectId
import hashlib
import secrets
import datetime

client = MongoClient()
#client = MongoClient('mongodb://mongodb:27017/')

db = client["countup"]

def get_user_id(user):
    user_id = db.users.find_one({"username": user}, {"_id": 1})["_id"]
    return user_id

def create_user(email, username, password):
    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    db.users.insert_one({"username": username, "email": email, "salt": salt, "password": hashed_password})

def get_username_from_email(email):
    try:
        username = db.users.find_one({"email": email}, {"username": 1})["username"]
    except:
        return None
    return username

def authenticate_user(username=None, password=None):
    if username is not None:
        user = db.users.find_one({"username": username}, {"salt": 1})
    #elif email is not None:
    #    user = db.users.find_one({"email": email}, {"salt": 1})
    if user is None:
        return False
    salt = user["salt"]
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    if username is not None:
        user = db.users.find_one({"username": username, "password": hashed_password})
    #elif email is not None:
    #    user = db.users.find_one({"email": email, "password": hashed_password}) 
    if user is not None:
        return True
    else:
        return False

def add_stroke_on_reservation(receiver, added_from):
    db.stroke_reservation.insert_one({"username": receiver, "added_from": added_from, "added_at": datetime.datetime.now(), "votes": 0})

def add_stroke(receiver, added_from):
    db.strokes.insert_one({"username": receiver, "added_from": added_from})
