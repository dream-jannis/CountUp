from flask import Blueprint, session, request, url_for, redirect, render_template, flash

from helpers.db import *

settings = Blueprint('settings', __name__, template_folder='pages')

@settings.route("", methods=["GET", "POST"])
def main():
    return render_template("settings.html")