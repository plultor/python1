# app.py
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'
@app.route('/request')
def request_info():
    return f'request method: {request.method} url: {request.url} headers: {request.headers}'


if __name__ == '__main__':
    app.run(debug=True)