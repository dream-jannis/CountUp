import os

from PIL import Image, ImageDraw, ImageSequence
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
        'amount_strokes_user': len(read_strokes_by_username(session['username']))
    }
    return render_template("settings.html", data = data)

@settings.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        if filename.split(".")[1] == "gif":
            convert_animated_gif(f"{os.path.join(UPLOAD_FOLDER, filename)}", f"{os.path.join(UPLOAD_FOLDER, filename)}")
        else:
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

def convert_animated_gif(input_path, output_path, size=(100, 100)):
    img = Image.open(input_path)
    
    frames = []
    
    for frame in ImageSequence.Iterator(img):
        frame = frame.resize(size, Image.ANTIALIAS)
        output = Image.new("RGBA", size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(output)
        draw.pieslice([0, 0, *size], 0, 360, fill=(255, 255, 255, 255))
        output.paste(frame, (0, 0), mask=output)
        output = output.convert("RGB")
        frames.append(output)
    
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=img.info['duration'])
