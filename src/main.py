from mido import Message, MidiFile, MidiTrack, MetaMessage
from markov import MarkovChain, NDMarkovChain
from transition_matrix import populate_matrix, prep_list, nd_convert_to_probabilities
from parse_midi import parse_midi
import random, constants

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

def note_matrix():
    return nd_convert_to_probabilities(populate_matrix(parse_midi(), 7, 2))

def tdNote_matrix():
    return nd_convert_to_probabilities(populate_matrix(prep_list(map(lambda x : x[0], parse_midi()), constants.maj_scale_list), 7, 4))

def duration_matrix():
    return nd_convert_to_probabilities(populate_matrix(prep_list(map(lambda x : x[1], parse_midi()), constants.note_duration), 4, 2))

def combo_matrix():
    return nd_convert_to_probabilities(populate_matrix(prep_list(parse_midi(), constants.combo), len(constants.combo), 3))

track.append(Message('program_change', program=0, time=0))
mkv = NDMarkovChain(combo_matrix(),constants.combo, [6,11])
#mkv = NDMarkovChain(tdNote_matrix(),constants.maj_scale, [0, 6, 0])
durmkv = MarkovChain(duration_matrix(),constants.note_duration, 2)

counter = 0
tonic_hit = False
while counter < constants.minimum_duration or not tonic_hit:
    note = mkv.get_state()[0]
    if note == 11:
        note = -1
    track.append(Message('note_on', note=60 + note, velocity=64, time=0))
    track.append(Message('note_off', note=60 + note, velocity=32, time=int(mkv.get_state()[1] * 480 * 4)))
    if counter > constants.minimum_duration and mkv.get_state()[0] == 0:
        tonic_hit = True
    counter += 1
    mkv.next_state()
    durmkv.next_state()

mid.save(constants.save_midi_path + 'new_song.mid')
