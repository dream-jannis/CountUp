from flask import Blueprint, render_template, request

from pymongo import MongoClient
import json

index = Blueprint("index", __name__, template_folder="pages")

client = MongoClient('mongodb://localhost:27017/')
db = client['countup']
collection = db['count_events']

@index.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        user = request.form['user']
        event = request.form['event']

        # Daten in die MongoDB einfügen
        collection.insert_one({'user': user, 'event': event})

    # Daten aus der MongoDB abrufen
    user_events = collection.aggregate([
        {'$group': {'_id': '$user', 'count': {'$sum': 1}}}
    ])

    # Daten für das Balkendiagramm vorbereiten
    labels = []
    counts = []
    for data in user_events:
        labels.append(data['_id'])
        counts.append(data['count'])

    return render_template('index.html', labels=json.dumps(labels), counts=json.dumps(counts))