from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import requests
from requests.auth import HTTPDigestAuth
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/pong', methods=['GET'])
def pong():
    num = random.randint(0, 9)
    return '<h1>' + num + '</h1>'




