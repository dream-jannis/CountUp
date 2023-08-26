from flask import Flask

from templates.index.views import index
from templates.login.views import login
from templates.settings.views import settings

app = Flask(__name__)
app.secret_key = "J11_FEdsafss323gzhgfgegfaße3eefcretƒggju_J11"

app.register_blueprint(index, url_prefix="/")
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(settings, url_prefix="/settings")


#@app.errorhandler(Exception)
#def server_error(err):
#    return(f"Fehler ;) {err}")

#if __name__ == '__main__':
#    app.run(debug=True)