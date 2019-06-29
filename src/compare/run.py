
"""
Takes in two JSON files / dictionaries in the note format, one which is the
guess,and the other which is the source. This method compares the guesses' notes
to the source's and flags each note in the guess JSON to whether it was correct
or not.
"""


# [Note] [Note] -> [Flagged Note]
def generate_comparison_json(guess, source):
    absolute_duration = 0
    for note in guess:
        note['correct'] = note_exists_in(absolute_duration, note, source)
        absolute_duration += note['duration']
    return guess


# Checks if the note exists in the list of notes.
# Note [Note] -> Note
def note_exists_in(abs_duration, note, lo_notes):
    if note_exists_at(abs_duration, lo_notes):
        return notes_equal(note, get_note_at(abs_duration, lo_notes))
    else:
        return False


# NOTE : Not needed, python equality suffices
# Checks if two notes are equal.
# Note Note -> Boolean
def notes_equal(note_a, note_b):
    return note_a == note_b


# Checks if a note exists at the absolute time (time from the first note)
# Decimal [Note] -> Boolean
def note_exists_at(time, lo_notes):
    time_acc = 0
    lo_times = []
    for note in lo_notes:
        lo_times.append(time_acc)
        time_acc += note['duration']
    return time in lo_times


# Gets a note at the specified absolute time.
# Decimal [Note] -> Note
def get_note_at(time, lo_notes):
    time_acc = 0
    for note in lo_notes:
        if time_acc == time:
            return note
        time_acc += note['duration']
    return None
