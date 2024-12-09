from app3_db import my_db, f_app
from models import MyUser

with f_app.app_context():
    my_db.create_all()

    print("DB created - SURAJ.")

