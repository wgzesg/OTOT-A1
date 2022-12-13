from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask("backend server")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/infer', methods=['POST'])
def api():
    data = request.data  # data is empty
    print(request.get_json())
    return jsonify({'data': [10]*10})

@app.route('/', methods=['GET'])
def index():
    return "index"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)