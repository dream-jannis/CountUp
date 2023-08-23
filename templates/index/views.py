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

    count_strokes_reserveation = len(read_all_strokes_on_reservation())

    data = {
        'user_names': usernames,
        'strokes': [5, 50, 15,5,2,4],
        'count_open_strokes': count_strokes_reserveation,
        'strokes_on_reservation': read_all_strokes_on_reservation()
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

    return 200
