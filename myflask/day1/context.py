from day2 import myflask_db, app
from models import MyUser

with app.app_context():
    myflask_db.create_all()
    print("DB created: suaj")