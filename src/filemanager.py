from .transition_matrix import nd_convert_to_probabilities, populate_matrix, prep_list, entry_point
from .parse_midi import parse_midi
from .markov import NDMarkovChain
from .util import cartesian_product
from . import constants
import pickle
import random

# TODO: these need a home

# TODO: should this be here?
combo = cartesian_product(constants.maj_scale_list, constants.note_duration)

scalecombo = cartesian_product([i for i in range(-8,9)], constants.note_duration)

def note_matrix():
    return nd_convert_to_probabilities(populate_matrix(parse_midi(), 7, 2))


def tdNote_matrix():
    return nd_convert_to_probabilities(
        populate_matrix(prep_list(map(lambda x: x[0], parse_midi()),
        constants.maj_scale_list), 7, 4))


def duration_matrix():
    return nd_convert_to_probabilities(populate_matrix(
        prep_list(map(lambda x: x[1], parse_midi()), constants.note_duration), 4, 2))


def combo_matrix():
    return nd_convert_to_probabilities(populate_matrix(
        prep_list(parse_midi(), combo), len(combo), 3))


def scalecombo_matrix():
    return nd_convert_to_probabilities(populate_matrix(
        prep_list(parse_midi(), scalecombo), len(scalecombo), 3))


def scalecombo_entries():
    return random.choice(entry_point(prep_list(parse_midi(), scalecombo), 2))

# durmkv = MarkovChain(duration_matrix(),constants.note_duration, 2)


mark = NDMarkovChain(scalecombo_matrix(), scalecombo, list(reversed(scalecombo_entries())))
# mkv = NDMarkovChain(tdNote_matrix(),constants.maj_scale, [0, 6, 0])


def save(mkv):
    pickle.dump(mkv, open(constants.matrix_path, "wb"))


def load():
    return pickle.load(open(constants.matrix_path, "rb"))
