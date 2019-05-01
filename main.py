from mido import Message, MidiFile, MidiTrack, MetaMessage
from markov import MarkovChain, noteMatrix, durationMatrix, note_duration

import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

class Note:
        def __init__(self, note_value):
                self.note_value = note_value
                self.neighbours = []

        def next(self):
                return random.choice(self.neighbours)

listofnotes = [Note(60),Note(62),Note(64),Note(65),Note(67),Note(69),Note(71),Note(72)]

def linkNotes():
        for note in listofnotes:
                for othernote in listofnotes:
                        if othernote is not note:
                                note.neighbours.append(othernote)

track.append(Message('program_change', program=12, time=0))
mkv = MarkovChain(noteMatrix(),list(range(12)), 0)
durmkv = MarkovChain(durationMatrix(),note_duration, 3)
#track.append(MetaMessage('set_tempo', tempo=60000, time=0))
for i in range(20):
    track.append(Message('note_on', note=60 + mkv.get_state(), velocity=64, time=0))
    track.append(Message('note_off', note=60 + mkv.get_state(), velocity=32, time=int(durmkv.get_state() * 480 * 4)))
    mkv.next_state()
    durmkv.next_state()

mid.save('new_song.mid')
