from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # return jsonify(msg="<h1>Hello World</h1>")
    return jsonify(["<h1>Hello World</h1>", "shedge"])


if __name__ == "__main__":
    app.run(debug=True, port=5050, host="0.0.0.0")