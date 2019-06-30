import unittest
from src import parse_midi


class TestParseMidi(unittest.TestCase):
    def test_relative_note(self):
        self.assertEqual(parse_midi.relative_note(72, "C"), 72)
        self.assertEqual(parse_midi.relative_note(69, "A"), 72)
        self.assertEqual(parse_midi.relative_note(71, "B"), 72)
        self.assertEqual(parse_midi.relative_note(74, "D"), 72)

    def test_valid_note(self):
        self.assertTrue(parse_midi.valid_note(69, "A"))
        self.assertTrue(parse_midi.valid_note(73, "A"))
        self.assertTrue(parse_midi.valid_note(74, "A"))
        self.assertTrue(parse_midi.valid_note(72, "C"))
        self.assertTrue(parse_midi.valid_note(84, "C"))
        self.assertTrue(parse_midi.valid_note(86, "C"))
        self.assertFalse(parse_midi.valid_note(72, "A"))

    def test_transpose(self):
        self.assertEqual(parse_midi.transpose(-13), -1)
        self.assertEqual(parse_midi.transpose(240), 12)
        self.assertEqual(parse_midi.transpose(23), 11)
        self.assertEqual(parse_midi.transpose(-3), -3)

    def test_scale_degree(self):
        self.assertEqual(parse_midi.scale_degree(72, "C"), 1)
        self.assertEqual(parse_midi.scale_degree(74, "C"), 2)
        self.assertEqual(parse_midi.scale_degree(71, "C"), -7)
        self.assertEqual(parse_midi.scale_degree(85, "A"), 3)
        self.assertEqual(parse_midi.scale_degree(61, "A"), -3)
        self.assertEqual(parse_midi.scale_degree(93, "E"), 4)
