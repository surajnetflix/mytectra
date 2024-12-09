from app import app, newdb
from models import NewUser

with app.app_context():
    newdb.create_all()
    print("created new DB.")