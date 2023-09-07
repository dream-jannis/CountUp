from flask import Blueprint, render_template

legal = Blueprint("legal", __name__, template_folder="pages")

@legal.route('/impressum')
def impressum():
    return render_template("impressum.html")

@legal.route('/datenschutz')
def datenschutz():
    return render_template("datenschutz.html")