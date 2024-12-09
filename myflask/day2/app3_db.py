from flask import Flask
import uuid
from flask_sqlalchemy import SQLAlchemy

f_app = Flask(__name__)

# db configuration
f_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_db.db"
f_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

my_db = SQLAlchemy(f_app)
