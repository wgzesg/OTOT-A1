from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from utils import get_random_population, get_best_counter

app = Flask("backend server")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/infer', methods=['POST'])
def api():
    json_data = request.get_json()
    game_list = json_data['past']['games']

    if len(game_list) == 0:
        prob_density = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    else:
        last = game_list[-1]['human']
        prob_density = get_best_counter(last)
    population = get_random_population(prob_density)
    vals = [population[i] for i in range(1, 11)]
    return jsonify({'data': vals})

@app.route('/', methods=['GET'])
def index():
    return "index"

if __name__ == '__main__':
    from waitress import serve 
    serve(app, host="0.0.0.0", port=5100)
