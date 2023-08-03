from flask import Blueprint, jsonify, request

from pymongo import MongoClient
import json

api = Blueprint("api", __name__, template_folder="pages")

client = MongoClient('mongodb://localhost:27017/')
db = client['countup']
collection = db['count_events']

@api.route('/api/events', methods=['GET'])
def get_events():
    user_events = collection.aggregate([
        {'$group': {'_id': '$user', 'count': {'$sum': 1}}}
    ])

    data = []
    for entry in user_events:
        data.append({'user': entry['_id'], 'count': entry['count']})

    return jsonify(data)

@api.route('/api/events', methods=['POST'])
def add_event():
    user = request.json.get('user')
    event = request.json.get('event')

    if user is None or event is None:
        return jsonify({'error': 'Missing user or event data'}), 400

    collection.insert_one({'user': user, 'event': event})
    return jsonify({'message': 'Event added successfully'}), 201