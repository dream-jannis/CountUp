from flask import Blueprint, render_template, redirect, url_for, session, request

from pymongo import MongoClient

login = Blueprint("login", __name__, template_folder="pages")

client = MongoClient('mongodb://localhost:27017/')
db = client['countup']
collection = db['count_events']

def is_authenticated(username, password):
    return username in users and users[username] == password

@login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_authenticated(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@login.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))