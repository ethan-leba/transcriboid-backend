from parse_midi import parse_midi
from util import weighted_random
from transition_matrix import populateMatrix, prepList
import constants

# [2D Matrix] -> [2D Matrix]
def convertToProbabilities(mat):
        newmat = []
        for row in mat:
                if sum(row) != 0:
                        newmat.append(list(map(lambda x : x / sum(row), row)))
                else:
                        newmat.append(row)
        return newmat

def TDconvertToProbabilities(tdmat):
    return list(map(lambda x : convertToProbabilities(x), tdmat))

def noteMatrix():
        return convertToProbabilities(populateMatrix(parse_midi(), 7, 2))

def tdNoteMatrix():
    return TDconvertToProbabilities(populateMatrix(prepList(map(lambda x : x[0], parse_midi()), constants.maj_scale_list), 7, 3))

def durationMatrix():
    return convertToProbabilities(populateMatrix(prepList(map(lambda x : x[1], parse_midi()), constants.note_duration), 4, 2))
# map(lambda x : x[1], raw_notes))))
class MarkovChain:
        def __init__(self, transition_matrix, states, init_state):
                self.transition_matrix = transition_matrix
                self.states = states
                self.current_state = init_state

        def next_state(self):
                self.current_state = weighted_random(self.transition_matrix[self.current_state])
                
        def get_state(self):
                return self.states[self.current_state]

class TDMarkovChain:
        def __init__(self, transition_matrix, states, init_state_1, init_state_2):
                self.transition_matrix = transition_matrix
                self.states = states
                self.prev_state = init_state_1
                self.current_state = init_state_2

        def next_state(self):
                tmp = self.current_state
                self.current_state = weighted_random(self.transition_matrix[self.prev_state][self.current_state])
                self.prev_state = tmp
                
        def get_state(self):
                return self.states[self.current_state]
