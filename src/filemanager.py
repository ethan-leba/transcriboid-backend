from .transition_matrix import nd_convert_to_probabilities, populate_matrix, prep_list
from .parse_midi import parse_midi
from .markov import NDMarkovChain
from . import constants
import pickle

# TODO: these need a home


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
        prep_list(parse_midi(), constants.combo), len(constants.combo), 3))

# durmkv = MarkovChain(duration_matrix(),constants.note_duration, 2)


mark = NDMarkovChain(combo_matrix(), constants.combo, [6, 11])
# mkv = NDMarkovChain(tdNote_matrix(),constants.maj_scale, [0, 6, 0])


def save(mkv):
    pickle.dump(mkv, open(constants.matrix_path, "wb"))


def load():
    return pickle.load(open(constants.matrix_path, "rb"))
