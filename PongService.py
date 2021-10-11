from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import requests
from requests.auth import HTTPDigestAuth
import random
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
auth = HTTPDigestAuth()

users = {
    "vcu": "rams"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/pong', methods=['GET'])
@auth.login_required()
def pong():
    randInt = random.randint(0, 9)
    return render_template("random-num.html", randInt=randInt)


if __name__ == "__main__":
    app.run(debug=True)



