import unittest
import src.compare.run as compare


class TestCompare(unittest.TestCase):
    def setUp(self):
        self.loNotes = [
            {'relative_value': 0, 'duration': 0.25},
            {'relative_value': 1, 'duration': 0.25},
            {'relative_value': 2, 'duration': 1},
            {'relative_value': 3, 'duration': 0.25},
            {'relative_value': 4, 'duration': 0.5}
        ]
        self.guessA = [
            {'relative_value': 4, 'duration': 0.25},
            {'relative_value': 1, 'duration': 0.25},
            {'relative_value': 4, 'duration': 1},
            {'relative_value': 3, 'duration': 0.25},
            {'relative_value': 4, 'duration': 0.5}
        ]
        self.guessB = [
            {'relative_value': 0, 'duration': 0.5},
            {'relative_value': 2, 'duration': 1},
            {'relative_value': 3, 'duration': 0.25},
            {'relative_value': 4, 'duration': 1}
        ]

    def test_note_equals(self):
        self.assertFalse(
            compare.notes_equal(
                {'relative_value': 3, 'duration': 0.25},
                {'relative_value': 0, 'duration': 0.25}))
        self.assertFalse(
            compare.notes_equal(
                {'relative_value': 0, 'duration': 0.25},
                {'relative_value': 0, 'duration': 0.5}))
        self.assertTrue(
            compare.notes_equal(
                {'relative_value': 0, 'duration': 0.25},
                {'relative_value': 0, 'duration': 0.25}))

    def test_note_exists_at(self):
        self.assertTrue(compare.note_exists_at(.0, self.loNotes))
        self.assertTrue(compare.note_exists_at(.25, self.loNotes))
        self.assertTrue(compare.note_exists_at(.5, self.loNotes))
        self.assertTrue(compare.note_exists_at(1.5, self.loNotes))
        self.assertTrue(compare.note_exists_at(1.75, self.loNotes))
        self.assertFalse(compare.note_exists_at(.75, self.loNotes))
        self.assertFalse(compare.note_exists_at(.98, self.loNotes))
        self.assertFalse(compare.note_exists_at(2.0, self.loNotes))
        self.assertFalse(compare.note_exists_at(2.75, self.loNotes))

    def test_get_note_at(self):
        self.assertEqual(
            compare.get_note_at(.25, self.loNotes),
            {'relative_value': 1, 'duration': 0.25})
        self.assertEqual(
            compare.get_note_at(.5, self.loNotes),
            {'relative_value': 2, 'duration': 1})
        self.assertEqual(
            compare.get_note_at(1.5, self.loNotes),
            {'relative_value': 3, 'duration': 0.25})
        self.assertEqual(
            compare.get_note_at(1.75, self.loNotes),
            {'relative_value': 4, 'duration': 0.5})

    def test_generate_comparison_json(self):
        self.assertEqual(
            compare.generate_comparison_json(self.guessA, self.loNotes),
            [
                {'relative_value': 4, 'duration': 0.25, 'correct': False},
                {'relative_value': 1, 'duration': 0.25, 'correct': True},
                {'relative_value': 4, 'duration': 1, 'correct': False},
                {'relative_value': 3, 'duration': 0.25, 'correct': True},
                {'relative_value': 4, 'duration': 0.5, 'correct': True}
            ])
        self.assertEqual(
            compare.generate_comparison_json(self.guessB, self.loNotes),
            [
                {'relative_value': 0, 'duration': 0.5, 'correct': False},
                {'relative_value': 2, 'duration': 1, 'correct': True},
                {'relative_value': 3, 'duration': 0.25, 'correct': True},
                {'relative_value': 4, 'duration': 1, 'correct': False}
            ])
