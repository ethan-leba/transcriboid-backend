import unittest
#from .context import src
import src.markov
import src.transition_matrix

class TestMarkov(unittest.TestCase):
    def setUp(self):
        self.two_d_markov = src.markov.NDMarkovChain([[0,1,0],[0,0,1],[1,0,0]], ["a","b","c"], [0])
        self.three_d_markov = src.markov.NDMarkovChain([[[0,1,0],[0,1,0],[0,0,1]],[[0,1,0],[0,0,1],[1,0,0]],[[0,0,1],[1,0,0],[0,1,0]]], None, [0,0])

    def test_next_statetwo_d_(self):
        self.assertEqual(list(self.two_d_markov.previous_states), [0])
        self.two_d_markov.next_state()
        self.assertEqual(list(self.two_d_markov.previous_states), [1])
        self.two_d_markov.next_state()
        self.assertEqual(list(self.two_d_markov.previous_states), [2])
        self.two_d_markov.next_state()
        self.assertEqual(list(self.two_d_markov.previous_states), [0])

    def test_next_state_three_d(self):
        self.assertEqual(list(self.three_d_markov.previous_states), [0, 0])
        self.three_d_markov.next_state()
        self.assertEqual(list(self.three_d_markov.previous_states), [1, 0])
        self.three_d_markov.next_state()
        self.assertEqual(list(self.three_d_markov.previous_states), [1, 1])
        self.three_d_markov.next_state()
        self.assertEqual(list(self.three_d_markov.previous_states), [2, 1])
        self.three_d_markov.next_state()
        self.assertEqual(list(self.three_d_markov.previous_states), [0, 2])
        self.three_d_markov.next_state()
        self.assertEqual(list(self.three_d_markov.previous_states), [2, 0])
        self.three_d_markov.next_state()
        self.assertEqual(list(self.three_d_markov.previous_states), [2, 2])
        self.three_d_markov.next_state()
        self.assertEqual(list(self.three_d_markov.previous_states), [1, 2])
        self.three_d_markov.next_state()

    def test_get_state(self):
        self.assertEqual(self.two_d_markov.get_state(), "a")
        self.two_d_markov.next_state()
        self.assertEqual(self.two_d_markov.get_state(), "b")
        self.two_d_markov.next_state()
        self.assertEqual(self.two_d_markov.get_state(), "c")

if __name__ == '__main__':
    unittest.main()
