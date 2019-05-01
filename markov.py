from parse_midi import parse_midi
from util import weighted_random
# NOTES ONLY ATM
# create the empty matrix
note_duration = [0.125,0.25,0.5,1]
note_dict = {
        0.125 : 0,
        0.25 : 1,
        0.5 : 2,
        1 : 3
        }
# 0 - 11 is note value, multiples of 12 for duration from small to big
def genMtMatrix(size):
        mat = []
        for x in range(size):
                inner_mat = []
                for y in range(size):
                        inner_mat.append(0)
                mat.append(inner_mat)
        return mat

# [(Int, Float)] -> Matrix
def populateMatrix(raw_notes):
        mat = genMtMatrix(12)
        for idx in range(len(raw_notes)-1):
                mat[raw_notes[idx][0]][raw_notes[idx + 1][0]] += 1
        return mat

# [(Int, Float)] -> Matrix
def populateDurationMatrix(raw_notes):
        mat = genMtMatrix(4)
        for idx in range(len(raw_notes)-1):
                mat[note_dict.get(raw_notes[idx][1], 0)][note_dict.get(raw_notes[idx + 1][1], 0)] += 1
        return mat

def convertToProbabilities(mat):
        newmat = []
        for row in mat:
                if sum(row) != 0:
                        newmat.append(list(map(lambda x : x / sum(row), row)))
                else:
                        newmat.append(row)
        return newmat

def noteMatrix():
        return convertToProbabilities(populateMatrix(parse_midi()))

def durationMatrix():
        return convertToProbabilities(populateDurationMatrix(parse_midi()))

class MarkovChain:
        def __init__(self, transition_matrix, states, init_state):
                self.transition_matrix = transition_matrix
                self.states = states
                self.current_state = init_state

        def next_state(self):
                self.current_state = weighted_random(self.transition_matrix[self.current_state])
                
        def get_state(self):
                return self.states[self.current_state]
