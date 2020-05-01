from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/add/<a>/<b>', methods=['POST'])
def add(a, b):
    return jsonify(result=int(a) + int(b))

@app.route('/sub/<a>/<b>', methods=['POST'])
def sub(a, b):
    return jsonify(result=int(a) - int(b))