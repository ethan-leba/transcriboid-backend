import sys

sys.path.append('./')

from src.constants import minimum_duration
from src.filemanager import load
from src.compare.run import generate_comparison_json
from src.output.json import generate_json
from flask import Flask, g
from flask import json, request, send_from_directory
from flask_cors import CORS


app = Flask(__name__, static_url_path='')
CORS(app)


def get_mkv():
    if 'mkv' not in g:
        g.mkv = load()

    return g.mkv

@app.route('/api/get')
def song():
    return generate_json(get_mkv())

@app.route('/api/compare', methods=['POST'])
def get_comparison():
    req_data = request.get_json()

    return json.dumps({
    "corrected": generate_comparison_json(req_data['user'],req_data['actual']),
    "actual": req_data['actual']
    })

@app.route('/resources/<path:path>')
def send_resources(path):
    return send_from_directory('resources', path)

if __name__ == '__main__':
    app.run()
