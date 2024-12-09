from app import newdb

class NewUser(newdb.Model):
    id = newdb.Column(newdb.Integer, primary_key=True)
    name = newdb.Column(newdb.String(100), nullable=False)
    email = newdb.Column(newdb.String(100), nullable=False)
