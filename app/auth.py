from functools import wraps
from flask import session, redirect, url_for, render_template
from authlib.integrations.flask_client import OAuth
from . import app 

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
        if 'google_token' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()

    # Puedes almacenar información del usuario en la sesión si es necesario
    session['google_token'] = token
    session['user_info'] = user_info

    # Aquí podrías redirigir a la página principal o a donde desees
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Eliminar la información del usuario de la sesión
    session.pop('google_token', None)
    session.pop('user_info', None)

    # Luego redirige a la página de inicio o a donde desees
    return redirect(url_for('index'))