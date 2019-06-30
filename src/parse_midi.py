from mido import MidiFile
import glob
from . import constants

files = glob.glob(constants.midi_path + '/*.mid')
midis = list(map(lambda x: MidiFile(x), files))


# Convert the data from the midi files into a tuple containing information
# about the note pitch and duration.
# IO -> [(Int, Int)]
def parse_midi():
    notes = []
    for mid in midis:
        for i, track in enumerate(mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            key_sig = ""
            for msg in track:
                if msg.type == 'key_signature':
                    key_sig = msg.key
                if msg.type == 'note_on' and valid_note(msg.note, key_sig):
                    notes.append((scale_degree(msg.note, key_sig),
                                  quantize(msg, mid.ticks_per_beat)))
    return notes


# Shifts the key center to C
# Int, Int -> Int
def relative_note(note, key_sig):
    return (note - constants.key2offset[key_sig] + 3)


# checks if the note is diatonic or not
# Note, Int -> Boolean
def valid_note(note, key_sig):
    return relative_note(note, key_sig) % 12 in constants.maj_scale_list


# TODO: This is fragile
# converts the note from absolute pitch to relative scale degree (+/- 1 octave)
# Int, Int -> Int
def scale_degree(note, key_sig):
    note = divmod(transpose(relative_note(note, key_sig) - 72), 12)
    if note[0] == 0:
        return constants.semitone2scale[note[1]]
    else:
        return constants.semitone2scale[note[1]] * note[0]


# transposes a note until it is between an octave below and and octave up (-12 to 12)
# Int -> Int
def transpose(note):
    if(note >= -12 and note <= 12):
        return note
    elif (note < -12):
        return transpose(note + 12)
    elif(note > 12):
        return transpose(note - 12)


# quantizes to 16th notes
# Int, Int -> Float
def quantize(note, ticks_per_beat):
    return round((note.time * 8) / ticks_per_beat) / 8
