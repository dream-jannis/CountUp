from flask import Blueprint, render_template, redirect, url_for, session, request

from helpers.decorators import login_required
from helpers.db import *

index = Blueprint("index", __name__, template_folder="pages")

@index.route('/', methods=['GET', 'POST'])
@login_required
def main():
    """
    Main Funktion -> Index Route
    """
    usernames = []
    usernames_profile_picture = {}
    user_stroke = {}
    for x in read_all_users():
        username = x["username"]
        usernames.append(username)
        usernames_profile_picture[username] = x["profile_picture"]
        for y in read_all_strokes():
            if username == y["username"]:
                user_stroke[username] = len(read_strokes_by_username(username))


    strokes_on_reservation_user_no_vote = []
    strokes_on_reservation_remaining = []
    for item in read_all_strokes_on_reservation():
        if session["username"] not in (item["first_vote"],item["second_vote"], item["third_vote"]):
            strokes_on_reservation_user_no_vote.append(item)
        else:
            strokes_on_reservation_remaining.append(item)

    count_strokes_reservation = len(strokes_on_reservation_user_no_vote)

    data = {
        'active_user': session['username'],
        'usernames': usernames,
        'usernames_profile_picture': usernames_profile_picture,
        'profile_picture': get_profile_picture(session['username'])['profile_picture'],
        'user_stroke': user_stroke,
        'count_open_strokes': count_strokes_reservation,
        'strokes_on_reservation': strokes_on_reservation_user_no_vote,
        'strokes_on_reservation_remaining': strokes_on_reservation_remaining
    }
    return render_template('index.html', data = data)

@index.route("/add_stroke", methods=['GET', 'POST'])
@login_required
def add_stroke():
    """
    Add Stroke Funktion
    """
    if request.method == 'POST':
        user = request.form['user']
        event = request.form['event']
        add_stroke_on_reservation(user, session["username"], event)

    return redirect(url_for('index.main'))

@index.route("/verify_stroke", methods=['GET', 'POST'])
@login_required
def verify_stroke():
    """
    Verify Stroke Funktion
    """
    if request.method == "POST":
        add_vote(request.form["stroke_id"], session["username"])
    return "Success", 200
