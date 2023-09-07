from flask import Blueprint, session, render_template

from helpers.db import *

legal = Blueprint("legal", __name__, template_folder="pages")

@legal.route('/impressum')
def impressum():
    if "logged_in" not in session:
        return render_template("impressum.html")
    else:
        data = {
            'active_user': session['username'],
            'profile_picture': get_profile_picture(session['username'])['profile_picture']
        }
    return render_template("impressum_logged.html", data = data)

@legal.route('/datenschutz')
def datenschutz():
    if "logged_in" not in session:
        return render_template("datenschutz.html")
    else:
        data = {
            'active_user': session['username'],
            'profile_picture': get_profile_picture(session['username'])['profile_picture']
        }
    return render_template("datenschutz_logged.html", data = data)