from flask import Blueprint, render_template, redirect, url_for, session, request

from helpers.decorators import login_required
from helpers.db import *
import json

index = Blueprint("index", __name__, template_folder="pages")

@index.route('/', methods=['GET', 'POST'])
@login_required
def main():

    usernames = []
    for x in read_all_users():
        usernames.append(x["username"])

    strokes_on_reservation = []
    for item in read_all_strokes_on_reservation():
        if session["username"] not in (item["first_vote"], item["second_vote"], item["third_vote"]):
            strokes_on_reservation.append(item)

    count_strokes_reserveation = len(strokes_on_reservation)
    
    print("SUS",read_strokes_by_username())
    data = {
        'user_names': usernames,
        'strokes': [5, 50, 15,5,2,4],
        'count_open_strokes': count_strokes_reserveation,
        'strokes_on_reservation': strokes_on_reservation
    }
    return render_template('index.html', data = data)

@index.route("/add_stroke", methods=['GET', 'POST'])
@login_required
def add_stroke():
    if request.method == 'POST':
        user = request.form['user']
        event = request.form['event']
        add_stroke_on_reservation(user, session["username"], event)

    return redirect(url_for('index.main'))

@index.route("/verify_stroke", methods=['GET', 'POST'])
@login_required
def verify_stroke():
    print("asdf")
    if request.method == "POST":
        add_vote(request.form["stroke_id"], session["username"])
    return "Success", 200
