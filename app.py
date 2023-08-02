from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from matplotlib import pyplot as plt
import io
import base64
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    count = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    users = User.query.order_by(User.count.desc()).all()
    return render_template('index.html', users=users)

@app.route('/increment/<int:user_id>')
def increment(user_id):
    user = User.query.get(user_id)
    if user:
        user.count += 1
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/chart')
def chart():
    users = User.query.order_by(User.count.desc()).all()
    names = [user.name for user in users]
    counts = [user.count for user in users]
    plt.bar(names, counts)
    plt.savefig('static/chart.png')
    return render_template('chart.html')

if __name__ == '__main__':
    #if not os.path.exists('test.db'):
    db.create_all()
    app.run(debug=True)
