from functools import wraps
from flask import redirect, url_for, session, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session and "username" not in session:
            return redirect(url_for("auth.logout", next=request.url))
        return f(*args, **kwargs)
    return decorated_function