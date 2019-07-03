from .transition_matrix import nd_convert_to_probabilities, populate_matrix, prep_list, entry_point
from .parse_midi import parse_midi
from .markov import NDMarkovChain
from .util import cartesian_product
from . import constants
import pickle
import random

# The cartesian product of the two octaves and the possible note durations.
scalecombo = cartesian_product(
    [i for i in range(-8, 9)],
    constants.note_duration)


# Generates the transition matrix for the markov chain
def scalecombo_matrix():
    return nd_convert_to_probabilities(populate_matrix(
        prep_list(parse_midi(), scalecombo), len(scalecombo), 3))


# Chooses a primer melody for the markov chain
def scalecombo_entries():
    return random.choice(entry_point(prep_list(parse_midi(), scalecombo), 2))


# The markov object used by the application
mark = NDMarkovChain(scalecombo_matrix(), scalecombo,
                     list(reversed(scalecombo_entries())))


# Saves the markov chain object
def save(mkv):
    pickle.dump(mkv, open(constants.matrix_path, "wb"))


# Loads the markov chain object
def load():
    return pickle.load(open(constants.matrix_path, "rb"))


if __name__ == "__main__":
    save(mark)
