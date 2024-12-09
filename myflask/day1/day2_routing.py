from flask import Flask, jsonify
import uuid

app = Flask(__name__)

unique_id = uuid.uuid4()
print("UNIQUE_ID :: ", unique_id)

@app.route('/')
def index():
    return jsonify("Hi, Welcome to my flask app")

# @app.route('/hello/<name>')
# @app.route('/<name>')
# def home(name):
#     name = name.title()
#     return jsonify("Hello " + name + " \n Welcome to our flask app!!")

@app.route('/hello/<name>/<path:filepath>/<uuid:uid>/<float:f>')
# @app.route('/hello/<name>/<path:filepath>')
def details(name, filepath, uid, f):
    # name = name.title()
    print("---suraj shedge data:--", name, filepath, uid, f)
    # msg = " Hello: " + filepath + " :::: " + name + " :::: " + uid
    return jsonify("---suraj shedge data:--", name, filepath, uid, f)


# @app.route('/hello/<name>/<int:id>')
# @app.route('/<name>')
# def details(name, id):
#     name = name.title()
#     return jsonify("Hello -----" + name + "-----------" + str(id) +  "\n Welcome to our flask app!!")



if __name__ == "__main__":
    app.run(debug=True, port=5050, host="127.0.0.1")
