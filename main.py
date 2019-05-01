from mido import Message, MidiFile, MidiTrack, MetaMessage
from markov import MarkovChain, noteMatrix, durationMatrix 
from transition_matrix import note_duration
import random

maj_scale = [0, 2, 4, 5, 7, 9, -1]
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))
mkv = MarkovChain(noteMatrix(),maj_scale, 0)
durmkv = MarkovChain(durationMatrix(),note_duration, 2)
#track.append(MetaMessage('set_tempo', tempo=60000, time=0))
counter = 0
tonic_hit = False
while counter < 25 or not tonic_hit:
    track.append(Message('note_on', note=60 + mkv.get_state(), velocity=64, time=0))
    track.append(Message('note_off', note=60 + mkv.get_state(), velocity=32, time=int(durmkv.get_state() * 480 * 4)))
    if counter > 25 and mkv.get_state() == 0:
        tonic_hit = True
    counter += 1
    mkv.next_state()
    durmkv.next_state()

mid.save('new_song.mid')
