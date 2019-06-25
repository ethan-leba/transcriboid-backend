from util import cartesian_product
# User change
minimum_duration = 25
midi_path = '../markov_src'
save_midi_path = '../markov_output/'
# Preset
maj_scale = [0, 2, 4, 5, 7, 9, -1]

key2offset = {
        'A' : 0,
        'A#' : 1,
        'B' : 2,
        'C' : 3,
        'C#' : 4,
        'D' : 5,
        'D#' : 6,
        'E' : 7,
        'F' : 8,
        'F#' : 9,
        'G' : 10,
        'G#' : 11}

note_duration = [0.125,0.25,0.5,1]
maj_scale_list = [0, 2, 4, 5, 7, 9, 11]

combo = cartesian_product(maj_scale_list,note_duration)
