import unittest
from src import transition_matrix


class TestTransitionMatrix(unittest.TestCase):
    def test_nd_convert_to_probabilities(self):
        self.assertEqual(
            transition_matrix.nd_convert_to_probabilities([2, 4, 2]),
            [.25, .5, .25])
        self.assertEqual(
            transition_matrix.nd_convert_to_probabilities([0, 0, 0]),
            [0, 0, 0])
        self.assertEqual(
            transition_matrix.nd_convert_to_probabilities([2, 4, 2, 2]),
            [.2, .4, .2, .2])
        self.assertEqual(
            transition_matrix.nd_convert_to_probabilities(
                [[2, 4, 2], [4, 2, 2], [8, 2, 0]]),
            [[.25, .5, .25], [.5, .25, .25], [.8, .2, 0]])
        self.assertEqual(transition_matrix.nd_convert_to_probabilities(
            [[[[[5, 5]]]]]), [[[[[.5, .5]]]]])

    def test_gen_nd_matrix(self):
        self.assertEqual(
            transition_matrix.gen_nd_matrix(0, 1),
            [])
        self.assertEqual(
            transition_matrix.gen_nd_matrix(3, 1),
            [0, 0, 0])
        self.assertEqual(
            transition_matrix.gen_nd_matrix(3, 2),
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(
            transition_matrix.gen_nd_matrix(2, 3),
            [[[0, 0], [0, 0]], [[0, 0], [0, 0]]])

    def test_populate_matrix(self):
        self.assertEqual(
            transition_matrix.populate_matrix([0, 1, 2], 3, 2),
            [[0, 1, 0],
             [0, 0, 1],
             [0, 0, 0]])
        self.assertEqual(
            transition_matrix.populate_matrix([0, 1, 1, 1, 0], 2, 3),
            [[[0, 0], [0, 1]], [[0, 0], [1, 1]]]
        )

    def test_prep_list(self):
        dict = ["A", "B", "C", "D"]
        self.assertEqual(
            transition_matrix.prep_list(["A", "A", "A"], dict),
            [0, 0, 0])
        self.assertEqual(transition_matrix.prep_list([], dict), [])
        self.assertEqual(
            transition_matrix.prep_list(["A", "A", "B", "D", "D", "C"], dict),
            [0, 0, 1, 3, 3, 2])

    def test_entry_point(self):
        self.assertEqual(
            transition_matrix.entry_point([1, 2, 3, 4, 5, 6, 7], 2),
            [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
        self.assertEqual(
            transition_matrix.entry_point([1, 2, 3, 4, 5, 6, 7], 3),
            [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]])


if __name__ == '__main__':
    unittest.main()
