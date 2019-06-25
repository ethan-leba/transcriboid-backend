from mido import MidiFile
import glob
from . import constants

files = glob.glob(constants.midi_path + '/*.mid')
midis = list(map(lambda x : MidiFile(x), files))

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
                if msg.type == 'note_on':
                   notes.append((relative_note(msg, key_sig), quantize(msg, mid.ticks_per_beat)))
    return notes

# converts the note from absolute pitch to relative pitch in the key
# Int, Int -> Int
def relative_note(note, key_sig):
        return (note.note - constants.key2offset[key_sig] - 9) % 12

# quantizes to 16th notes
# Int, Int -> Float
def quantize(note, ticks_per_beat):
    return round((note.time * 8) / ticks_per_beat) / 8
