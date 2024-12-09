from day2 import myflask_db


class MyUser(myflask_db.Model):
    id = myflask_db.Column(myflask_db.Integer, primary_key=True)
    username = myflask_db.Column(myflask_db.String(100), nullable=False)
    email = myflask_db.Column(myflask_db.String(150), nullable=False)