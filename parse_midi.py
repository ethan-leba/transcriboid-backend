from mido import MidiFile
import glob

files = glob.glob('markov_src/*.mid')
midis = list(map(lambda x : MidiFile(x), files)) #MidiFile("markov_src/satie_cured.mid")

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

quantize_grid = [0.125, 0.25, 0.5, 1.0]

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
                    #print("Note: " + str(relative_note(msg, key_sig)) + "Beat ln: " + str(quantize(msg, mid.ticks_per_beat)))
                   notes.append((relative_note(msg, key_sig), quantize(msg, mid.ticks_per_beat)))
    return notes

def relative_note(note, key_sig):
    #print(key2offset[key_sig])
        return (note.note - key2offset[key_sig] - 9) % 12
# quantizes to 16th notes
def quantize(note, ticks_per_beat):
    return round((note.time * 8) / ticks_per_beat) / 8
#print(parse_midi())
