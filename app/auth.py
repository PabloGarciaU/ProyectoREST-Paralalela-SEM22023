from functools import wraps
from flask import session, redirect, url_for, request, jsonify
from authlib.integrations.flask_client import OAuth
from .extensions import api

oauth = OAuth()

google = oauth.register(
    name='google',
    client_id="32644728196-qs8nr857m20s5ornv5akv34v837gs6ge.apps.googleusercontent.com",
    client_secret="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",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'profile' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper
