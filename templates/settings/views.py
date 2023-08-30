import os

from flask import Blueprint, session, request, jsonify, url_for, redirect, render_template, flash
from werkzeug.utils import secure_filename

from helpers.db import *


settings = Blueprint('settings', __name__, template_folder='pages')

UPLOAD_FOLDER = 'static/profile_pictures/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@settings.route("", methods=["GET", "POST"])
def main():
    data = {
        'active_user': session['username'],
        'profile_picture': get_profile_picture(session['username'])['profile_picture'],
    }
    return render_template("settings.html", data = data)

@settings.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        update_profile_picture(session['username'], str(filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    else:
        return jsonify({'message': 'No file uploaded'}), 400
    

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS