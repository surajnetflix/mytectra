from flask import Flask, jsonify, render_template, redirect

app = Flask(__name__)


# @app.route("/")
# def index():
#     msg = "Hello World. Welcome to FLASK!!"
#     return jsonify(msg)


@app.route("/home/<any('online', 'offline', 'unknown'):status>")
def home(status):
    return f"Hello World, You are {status}"


@app.route("/")
def templating():
    return render_template("index.html")


@app.route("/homepage")
def myhome():
    return "this is homepage, redirected from welcome page"

@app.route("/welcome")
def welcome():
    return redirect("/homepage")



if __name__ == "__main__":
    app.run(debug=True, port=5000)