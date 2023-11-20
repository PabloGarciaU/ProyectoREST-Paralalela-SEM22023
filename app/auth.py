from functools import wraps
from flask import Flask, session, redirect, url_for, request, jsonify
from authlib.integrations.flask_client import OAuth
from .extensions import api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Reemplaza con tu clave secreta

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
    return google.authorize_redirect(url_for('auth', _external=True))

@app.route('/auth')
def auth():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)
    session['google_token'] = (token, '')
    session['profile'] = user_info
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    session.pop('profile', None)
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    profile = session['profile']
    # Aquí puedes usar la información del perfil como desees
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)