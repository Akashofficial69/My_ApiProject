from flask import Flask, send_from_directory

from .routes import bp as routes_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp)
    return app
