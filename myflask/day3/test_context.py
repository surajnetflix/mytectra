from app import app, newdb
from models import NewUser

with app.app_context():
    usr = NewUser(name="sss", email="sss@gmail.com")
    newdb.session.add(usr)
    newdb.session.commit()
    print("Added data in DB.")