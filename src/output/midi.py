from mido import Message, MidiFile, MidiTrack
from .. import constants

# Generates a MIDI file based on the markov chain


def generate_midi(mkv):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=0, time=0))

    counter = 0
    tonic_hit = False
    while counter < constants.minimum_duration or not tonic_hit:
        note = mkv.get_state()[0]
        if note == 11:
            note = -1
        track.append(Message('note_on', note=60 + note, velocity=64, time=0))
        track.append(Message('note_off', note=60 + note,
                             velocity=32, time=int(mkv.get_state()[1] * 480 * 4)))
        if counter > constants.minimum_duration and mkv.get_state()[0] == 0:
            tonic_hit = True
        counter += 1
        mkv.next_state()
    mid.save(constants.save_midi_path + 'new_song.mid')
