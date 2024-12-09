from flask import Flask, jsonify
import uuid
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## database config
# app.config['SQLAlchemy_DATABASE_URI'] = "sqlite:///my_db.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my_db.db"
app.config['SQLAlchemy_TRACK_MODIFICATION'] = False
myflask_db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def index():
    num = 10
    float_num = 10.20
    strings = "Welcome to my FLASK APP"
    lists = ["SURAJ", "SHEDGE"]
    dictionarys = {"dictionary1": 1, "dictionary2": 2}

    # return jsonify(num=num, float_num=float_num, strings=strings, lists=lists, dictionarys=dictionarys)
    # return jsonify(num)
    return jsonify(num, float_num, strings, lists, dictionarys)


if __name__ == '__main__':
    app.run(debug=True, port=5050)