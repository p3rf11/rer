from flask import Flask
from .views import app_views

def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_views)
    return app
