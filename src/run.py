from .filemanager import load

from .output.midi import generate_midi
from .output.json import generate_json

from .transition_matrix import nd_convert_to_probabilities, populate_matrix, prep_list, entry_point
from .parse_midi import parse_midi
from .markov import NDMarkovChain
from .util import cartesian_product
from . import constants
# The cartesian product of the two octaves and the possible note durations.
scalecombo = cartesian_product(
    [i for i in range(-7, 8)],
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

def main():
    return generate_json(load())


if __name__ == "__main__":
    main()
