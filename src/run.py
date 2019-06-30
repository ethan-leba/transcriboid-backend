from .filemanager import load

from .output.midi import generate_midi
from .output.json import generate_json


# TODO: Deterministic bro.


def mainm():
    return generate_json(load())

if __name__ == "__main__":
    mainm()