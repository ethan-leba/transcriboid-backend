import unittest
from src import transition_matrix

class TestTransitionMatrix(unittest.TestCase):
    def test_nd_convert_to_probabilities(self):
        self.assertEqual(transition_matrix.nd_convert_to_probabilities([2,4,2]), [.25,.5,.25])
        self.assertEqual(transition_matrix.nd_convert_to_probabilities([0,0,0]), [0,0,0])
        self.assertEqual(transition_matrix.nd_convert_to_probabilities([2,4,2,2]), [.2,.4,.2,.2])
        self.assertEqual(transition_matrix.nd_convert_to_probabilities([[2,4,2], [4,2,2], [8, 2, 0]]), [[.25,.5,.25], [.5,.25,.25], [.8,.2,0]])
        self.assertEqual(transition_matrix.nd_convert_to_probabilities([[[[[5,5]]]]]),[[[[[.5,.5]]]]])

    def test_gen_nd_matrix(self):
        self.assertEqual(transition_matrix.gen_nd_matrix(0,1), [])
        self.assertEqual(transition_matrix.gen_nd_matrix(3,1), [0,0,0])
        self.assertEqual(transition_matrix.gen_nd_matrix(3,2), [[0,0,0],[0,0,0],[0,0,0]])
        self.assertEqual(transition_matrix.gen_nd_matrix(2,3),
        [[[0,0],[0,0]],[[0,0],[0,0]]])

    def test_populate_matrix(self):
        #TODO: do these tests
        print("filler")

    def test_prep_list(self):
        dict = ["A","B","C","D"]
        self.assertEqual(transition_matrix.prep_list(["A","A","A"],dict), [0,0,0])
        self.assertEqual(transition_matrix.prep_list([],dict), [])
        self.assertEqual(transition_matrix.prep_list(["A","A","B","D","D","C"],dict), [0,0,1,3,3,2])



if __name__ == '__main__':
    unittest.main()
