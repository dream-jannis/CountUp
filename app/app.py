from flask import Flask

from templates.index.views import index
from templates.login.views import login
from templates.settings.views import settings
from templates.legal_stuff.views import legal

UPLOAD_FOLDER = 'static/profile_pictures/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "J11_FEdsafss323gzhgfgegfaße3eefcretƒggju_J11"

app.register_blueprint(index, url_prefix="/")
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(settings, url_prefix="/settings")
app.register_blueprint(legal, url_prefix="/legal")


@app.errorhandler(Exception)
def server_error(err):
    return(f"""Herzlichen Glückwunsch, du hat einen Fehler gefunden. Um genau zu sein, diesen hier: {err}   
           \n Du kannst diesen Fehler gerne an Jannis weiterleiten ;)""")

if __name__ == '__main__':
    app.run(debug=True)