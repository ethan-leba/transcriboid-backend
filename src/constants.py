from .util import cartesian_product
# User change
# The minimum amount of notes that a song can have.
minimum_duration = 25
# -- File paths relative to the parent directory --
# The directory containing the midi files to be converted into a markov chain.
midi_path = './markov_src'
# The directory to save the file to.
save_midi_path = './markov_output/'
# The file to load the matrix from.
matrix_path = './markov_src/save.p'
# The directory to save the matrix to.
save_matrix_path = './markov_src/'

# Preset
# The notes of the major scale represented by semi-tones away from the tonic.
maj_scale = [0, 2, 4, 5, 7, 9, -1]

# Converts the key into semi-tones above A.
key2offset = {
        'A': 0,
        'A#': 1,
        'B': 2,
        'C': 3,
        'C#': 4,
        'D': 5,
        'D#': 6,
        'E': 7,
        'F': 8,
        'F#': 9,
        'G': 10,
        'G#': 11}

# Converts the semitones into scale degrees
semitone2scale = {
    0: 1,
    2: 2,
    4: 3,
    5: 4,
    7: 5,
    9: 6,
    11: 7
}

# The list of possible note durations in units of whole notes.
note_duration = [0.125, 0.25, 0.5, 1]

# The major scale again? TODO: what's the difference...
maj_scale_list = [0, 2, 4, 5, 7, 9, 11]
