from flask import Flask

from templates.index.views import index
from templates.login.views import login

app = Flask(__name__)
app.secret_key = "J11_FEdsafss323gzhgfgegfaße3eefcretƒggju_J11"

app.register_blueprint(index, url_prefix="/")
app.register_blueprint(login, url_prefix="/login")

@app.errorhandler(Exception)
def server_error(err):
    return(f"Fehler ;) {err}")

#if __name__ == '__main__':
#    app.run(debug=True)