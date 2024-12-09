from app3_db import my_db


class MyUser(my_db.Model):
    id = my_db.Column(my_db.Integer, primary_key=True)
    username = my_db.Column(my_db.String(50), nullable=False)
    email = my_db.Column(my_db.String(50), nullable=False)


