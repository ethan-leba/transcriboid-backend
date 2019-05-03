from collections import deque

from parse_midi import parse_midi
from util import weighted_random, matrix_depth
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
# [N-D Matrix] -> [N-D Matrix]
def NDconvertToProbabilities(mat):
    if isinstance(mat[0], list):
        return list(map(lambda x : NDconvertToProbabilities(x), mat))
    else:
        if sum(mat) != 0:
             return list(map(lambda x : x / sum(mat), mat))
        else:
             return mat 

def noteMatrix():
        return convertToProbabilities(populateMatrix(parse_midi(), 7, 2))

def tdNoteMatrix():
    return NDconvertToProbabilities(populateMatrix(prepList(map(lambda x : x[0], parse_midi()), constants.maj_scale_list), 7, 4))

def durationMatrix():
    return convertToProbabilities(populateMatrix(prepList(map(lambda x : x[1], parse_midi()), constants.note_duration), 4, 2))

class MarkovChain:
        def __init__(self, transition_matrix, states, init_state):
                self.transition_matrix = transition_matrix
                self.states = states
                self.current_state = init_state

        def next_state(self):
                self.current_state = weighted_random(self.transition_matrix[self.current_state])
                
        def get_state(self):
                return self.states[self.current_state]

class NDMarkovChain:
        def __init__(self, transition_matrix, states, previous_states):
                self.transition_matrix = transition_matrix
                self.states = states
                self.previous_states = deque(previous_states)
                self.dimensions = matrix_depth(self.transition_matrix)
                assert self.dimensions == len(previous_states) + 1

        def next_state(self):
                cursor = self.transition_matrix
                for idx in reversed(self.previous_states):
                    cursor = cursor[idx]
                new_state = weighted_random(cursor)
                self.previous_states.appendleft(new_state)
                self.previous_states.pop()

        def get_state(self):
                return self.states[self.previous_states[0]]
