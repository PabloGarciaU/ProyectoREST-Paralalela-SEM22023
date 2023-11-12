from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

from .extensions import api, db
from .resources import ns

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'supersecret'  # Reemplaza esto con tu propia clave secreta
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    google_blueprint = make_google_blueprint(
        client_id="32644728196-qs8nr857m20s5ornv5akv34v837gs6ge.apps.googleusercontent.com",
        client_secret="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",
        scope=["profile", "email"],
        redirect_url="/login/google/authorized"
    )
    app.register_blueprint(google_blueprint, url_prefix="/login")

    @app.route("/login/google/authorized")
    def index():
        if not google.authorized:
            return redirect(url_for("google.login"))
        resp = google.get("/oauth2/v1/userinfo")
        assert resp.ok, resp.text
        return "You are {email} on Google".format(email=resp.json()["email"])

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    return app