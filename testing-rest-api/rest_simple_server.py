from flask import Flask, request, make_response
from flask import jsonify
import uuid

REGISTERED_USERS = {}
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if "password" not in data or "user" not in data:
        return "Error", 401

    if data['password'] == data['user'] + '123':
        sid = uuid.uuid4()
        REGISTERED_USERS[str(sid)] = data['user']
        return "", 200, {'x-auth': sid}
    else:
        return "Error", 401


@app.route('/add/<a>/<b>', methods=['POST'])
def add(a, b):
    if ('HTTP_X_AUTH' not in request.headers.environ) or (request.headers.environ['HTTP_X_AUTH'] not in REGISTERED_USERS):
        return "Error", 401
    return jsonify(result=int(a) + int(b))


@app.route('/sub/<a>/<b>', methods=['POST'])
def sub(a, b):
    if ('HTTP_X_AUTH' not in request.headers.environ) or (request.headers.environ['HTTP_X_AUTH'] not in REGISTERED_USERS):
        return "Error", 401
    return jsonify(result=int(a) - int(b))


if __name__ == "__main__":
    app.run("localhost", "5000")
