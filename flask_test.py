import sys

sys.path.append('./')

from src.constants import minimum_duration
from src.filemanager import load
from src.output.json import generate_json
from flask import Flask, g
from flask import json
from flask_cors import CORS




app = Flask(__name__)
CORS(app)


def get_mkv():
    if 'mkv' not in g:
        g.mkv = load()

    return g.mkv


@app.route('/song')
def song():
    return major_scale() # generate_json(load()) # jsonify(mainm())]})


if __name__ == '__main__':
    app.run()


def major_scale():
    return json.dumps({
        "key_offset": 40,
        "notes": [
            {"relative_value": -1, "duration": 0.5},
            {"relative_value": -2, "duration": 0.5},
            {"relative_value": -3, "duration": 0.5},
            {"relative_value": -4, "duration": 0.5},
            {"relative_value": -5, "duration": 0.5},
            {"relative_value": -6, "duration": 0.5},
            {"relative_value": -7, "duration": 0.5},
            {"relative_value": 1, "duration": 0.5},
            {"relative_value": 2, "duration": 0.5},
            {"relative_value": 3, "duration": 0.5},
            {"relative_value": 4, "duration": 0.5},
            {"relative_value": 5, "duration": 0.5},
            {"relative_value": 6, "duration": 0.5},
            {"relative_value": 7, "duration": 0.5},
            {"relative_value": 8, "duration": 0.5}
        ]
    })
