from flask import Blueprint, session, request, url_for, redirect, render_template, flash

from helpers.db import *

login = Blueprint('auth', __name__, template_folder='pages')

@login.route("", methods=["GET", "POST"])
def main():
    email = None
    username = None
    password = None

    if request.method == "POST":
        try:
            username = request.form["user"]
            if "@" in username:
                email = username
                username = get_username_from_email(email)
                if username == None:
                    flash('Username/E-Mail or Password wrong!')
                    return redirect(url_for('auth.main'))
            else:
                email = None
            password = request.form["password"]
        except KeyError:
            session.clear()
            flash('Username/E-Mail or Password wrong!')
            return redirect(url_for('auth.main'))
        
        if authenticate_user(username=username, password=password):
            user_id = str(get_user_id(username))
            session["user_id"] = user_id
            session["username"] = username
            session["logged_in"] = True
            return redirect(url_for('index.main'))
        else:
            session.clear()
            flash('Username/E-Mail or Password wrong!')
            return redirect(url_for('auth.main'))
    session["last_page"] = "login.main"
    return render_template("login.html")

@login.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        try:
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            create_user(email, username, password)
            return redirect(url_for("auth.main"))
        except KeyError:
            session.clear()
            return redirect(url_for('auth.main'))

    session["last_page"] = "login.register"
    return render_template("register.html")

@login.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('auth.main'))
