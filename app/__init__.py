import os 
from flask import Flask, request, session, jsonify, logging
from .api import api_v1_auth, api_v1_user
from dotenv import load_dotenv
from .db import db


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_EXTERNAL_URL")
    db.init_app(app)
    app.register_blueprint(blueprint=api_v1_user)
    app.register_blueprint(blueprint=api_v1_auth)
    # for key,value in app.config.items():
    #     print(f"➡️ {key} - {value}")
   
    with app.app_context():
        from .db.models import User
        db.create_all()

    return app


