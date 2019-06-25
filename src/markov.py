from collections import deque

from util import weighted_random, matrix_depth
import constants


# Markov chain class with 2d transition matrix
class MarkovChain:
        def __init__(self, transition_matrix, states, init_state):
                self.transition_matrix = transition_matrix
                self.states = states
                self.current_state = init_state

        def next_state(self):
                self.current_state = weighted_random(self.transition_matrix[self.current_state])

        def get_state(self):
                return self.states[self.current_state]

# Markov chain class with an abritrarily sized transition matrix
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