import sys

sys.path.append('./')

from src.constants import minimum_duration
from src.filemanager import load
from src.compare.run import generate_comparison_json
from src.output.json import generate_json
from flask import Flask, g
from flask import json, request
from flask_cors import CORS




app = Flask(__name__)
CORS(app)


def get_mkv():
    if 'mkv' not in g:
        g.mkv = load()

    return g.mkv


@app.route('/song')
def song():
    #return major_scale(.125)
    return generate_json(load()) # jsonify(mainm())]})

@app.route('/submit', methods=['POST'])
def get_comparison():
    req_data = request.get_json()

    # print("get comparison reached!")
    return json.dumps({
    "corrected": generate_comparison_json(req_data['user'],req_data['actual']),
    "actual": req_data['actual']
    })

if __name__ == '__main__':
    app.run()


def major_scale(dur):
    return json.dumps({
        "key_offset": 40,
        "notes": [
            {"relative_value": -7, "duration": dur},
            {"relative_value": -6, "duration": dur},
            {"relative_value": -5, "duration": dur},
            {"relative_value": -4, "duration": dur},
            {"relative_value": -3, "duration": dur},
            {"relative_value": -2, "duration": dur},
            {"relative_value": -1, "duration": dur},
            {"relative_value": 0, "duration": dur},
            {"relative_value": 1, "duration": dur},
            {"relative_value": 2, "duration": dur},
            {"relative_value": 3, "duration": dur},
            {"relative_value": 4, "duration": dur},
            {"relative_value": 5, "duration": dur},
            {"relative_value": 6, "duration": dur},
            {"relative_value": 7, "duration": dur}
        ]
    })
