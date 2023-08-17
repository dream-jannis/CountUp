from flask import Blueprint, render_template, request

from helpers.decorators import login_required
from helpers.db import *
import json

index = Blueprint("index", __name__, template_folder="pages")


@index.route('/', methods=['GET', 'POST'])
@login_required
def main():
    if request.method == 'POST':
        user = request.form['user']
        event = request.form['event']


    return render_template('index.html')