from day2 import myflask_db, app
from models import MyUser


with app.app_context():
    user = MyUser(username="suraj", email="dfjl@example.com")
    myflask_db.session.add(user)
    myflask_db.session.commit()
    print("Added to DB-suraj")