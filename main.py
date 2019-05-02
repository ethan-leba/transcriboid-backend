from mido import Message, MidiFile, MidiTrack, MetaMessage
from markov import MarkovChain, noteMatrix, durationMatrix, tdNoteMatrix, TDMarkovChain
import random, constants

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))
mkv = TDMarkovChain(tdNoteMatrix(),constants.maj_scale, 2, 0)
durmkv = MarkovChain(durationMatrix(),constants.note_duration, 2)
track.append(MetaMessage('set_tempo', tempo=200, time=0))

counter = 0
tonic_hit = False
while counter < constants.minimum_duration or not tonic_hit:
    track.append(Message('note_on', note=60 + mkv.get_state(), velocity=64, time=0))
    track.append(Message('note_off', note=60 + mkv.get_state(), velocity=32, time=int(durmkv.get_state() * 480 * 4)))
    if counter > constants.minimum_duration and mkv.get_state() == 0:
        tonic_hit = True
    counter += 1
    mkv.next_state()
    durmkv.next_state()

mid.save('new_song.mid')
