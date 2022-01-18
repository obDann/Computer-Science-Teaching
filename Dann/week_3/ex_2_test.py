from exercise_2 import *
import unittest

class TestCardNamer(unittest.TestCase):

    def test_ace_diamonds(self):
        actual = card_namer('A', 'D')
        expected = 'Ace of Diamonds'
        self.assertEqual(actual, expected)

    def test_thirteen_aces(self):
        actual = card_namer('13', 'A')
        expected = 'CHEATER!'
        self.assertEqual(actual, expected)

    def test_jack_spades(self):
        actual = card_namer('J', 'S')
        expected = 'Jack of Spades'
        self.assertEqual(actual, expected)

    def test_ten_clubs(self):
        actual = card_namer('T', 'C')
        expected = '10 of Clubs'
        self.assertEqual(actual, expected)

class TestInsert(unittest.TestCase):

    def test_simple_zero(self):
        expected = '00'
        actual = insert('0','0',0)
        self.assertEqual(actual, expected)

    def test_end_of_str(self):
        expected = 'booop'
        actual = insert('booo', 'p', 4)
        self.assertEqual(actual, expected)

    def test_truck_list(self):
        expected = ['t', 'r', 'u', 'c', 'k']
        actual = insert(['t', 'r', 'c', 'k'], ['u'], 2)
        self.assertEqual(actual, expected)

    def test_insert_into_middle(self):
        expected = [50, 96, 3, 0, 1, 2]
        actual = insert([50, 96, 3, 2], [0,1], 3)
        self.assertEqual(actual, expected)

class TestUpToFirst(unittest.TestCase):

    def test_all_zeros(self):
        actual = up_to_first('0','0')
        expected = ''
        self.assertEqual(actual, expected)

    def test_scream(self):
        actual = up_to_first('SCREAAAAAAAAAAAAAAAAM', 'A')
        expected = ['home', 'dome']
        self.assertEqual(actual, expected)

    def test_no_obj_in_list(self):
        actual = up_to_first(['go', 'no', 'oho'], 'o')
        expected = ['go', 'no', 'oho']
        self.assertEqual(actual, expected)

    def test_middle_cutoff(self):
        actual = up_to_first(['home', 'dome', 'oh', 'quo'], 'oh')
        expected = ['home', 'dome']
        self.assertEqual(actual, expected)

    def test_int_list(self):
        actual = up_to_first([4, 3, 2, 1, 1, 2, 3], 1)
        expected = [4, 3, 2]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)