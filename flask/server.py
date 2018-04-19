from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


app.run()
