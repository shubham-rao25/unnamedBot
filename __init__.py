from flask import Flask 
from flask_cors import CORS

from .events import socketio
from .routes import main 

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(main)

    # Enable CORS for all routes
    CORS(app)

    socketio.init_app(app)

    return app