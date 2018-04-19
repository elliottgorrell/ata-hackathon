from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/answer', methods=['POST'])
def handle_answer():
    req_data = request.get_json()

    answer_base64 = req_data['answer']

app.run()
