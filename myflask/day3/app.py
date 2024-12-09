from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

newdb = SQLAlchemy(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1><p>flask:suraj</p>'

if __name__ == '__main__':
    app.run(debug=True)
