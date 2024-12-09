from app3_db import my_db, f_app
from models import MyUser

with f_app.app_context():
    user = MyUser(username="abcdx", email="axbcd@gmaiil.com")
    my_db.session.add(user)
    my_db.session.commit()
    print("Added to database")

