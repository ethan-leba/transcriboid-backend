from parse_midi import parse_midi
from util import weighted_random
from transition_matrix import populateMajorScaleMatrix,populateDurationMatrix

def convertToProbabilities(mat):
        newmat = []
        for row in mat:
                if sum(row) != 0:
                        newmat.append(list(map(lambda x : x / sum(row), row)))
                else:
                        newmat.append(row)
        return newmat

def noteMatrix():
        return convertToProbabilities(populateMajorScaleMatrix(parse_midi()))

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

class 3DMarkovChain:
        def __init__(self, transition_matrix, states, init_state_1, init_state_2):
                self.transition_matrix = transition_matrix
                self.states = states
                self.prev_state = init_state_1
                self.current_state = init_state_2

        def next_state(self):
                self.current_state = weighted_random(self.transition_matrix[self.current_state])
                
        def get_state(self):
