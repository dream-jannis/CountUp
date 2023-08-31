import os

from PIL import Image, ImageDraw
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
        convert_image(f"{os.path.join(UPLOAD_FOLDER, filename)}", f"{os.path.join(UPLOAD_FOLDER, filename)}")
        update_profile_picture(session['username'], str(filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    else:
        return jsonify({'message': 'No file uploaded'}), 400
    

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_image(input_path, output_path, size=(100, 100), output_format='PNG'):
    img = Image.open(input_path)
    img = img.resize(size, Image.ANTIALIAS)
    output = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(output)
    draw.pieslice([0, 0, *size], 0, 360, fill=(255, 255, 255, 255))
    output.paste(img, (0, 0), mask=output)
    if output_format == 'JPEG':
        output = output.convert("RGB")
    output.save(output_path, format=output_format)
