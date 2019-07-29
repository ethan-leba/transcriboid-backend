import sys

sys.path.append('./')

from src.constants import minimum_duration
from src.filemanager import load
from src.compare.run import generate_comparison_json
from src.output.json import generate_json
from flask import Flask, g
from flask import json, request, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


def get_mkv():
    if 'mkv' not in g:
        g.mkv = load()

    return g.mkv

class GenerateSong(Resource):
    def get(self):
        return generate_json(get_mkv())

class SubmitSong(Resource):
    def post(self):
        req_data = request.get_json()

        return json.dumps({
        "corrected": generate_comparison_json(req_data['user'],req_data['actual']),
        "actual": req_data['actual']
        })

api.add_resource(GenerateSong, '/get')
api.add_resource(SubmitSong, '/compare')

if __name__ == '__main__':
    app.run()
