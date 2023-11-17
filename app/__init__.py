from flask import Flask
from .auth import oauth
from .extensions import api, db
from .resources import ns
from datetime import timedelta  


def create_app():
    app = Flask(__name__)
    app.secret_key = 'super secret key'
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)

    oauth.init_app(app)

    app.config['SECRET_KEY'] = 'supersecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    return app