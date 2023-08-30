from flask import Blueprint, session, request, url_for, redirect, render_template, flash

from helpers.db import *

settings = Blueprint('settings', __name__, template_folder='pages')

@settings.route("", methods=["GET", "POST"])
def main():
    data = {
        'active_user': session['username'],
        'profile_picture': 'default'
    }
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
    return render_template("settings.html", data = data)