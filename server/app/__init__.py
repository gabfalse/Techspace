from flask import Flask
from flask_cors import CORS
from app.routes import main
from dotenv import load_dotenv
def create_app():
    load_dotenv() 
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main)
    return app
