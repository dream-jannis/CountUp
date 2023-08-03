from flask import Flask

from templates.index.views import index

app = Flask(__name__)

app.register_blueprint(index, url_prefix="/")

@app.errorhandler(Exception)
def server_error(err):
    return(f"Fehler ;) {err}")

#if __name__ == '__main__':
#    app.run(debug=True)