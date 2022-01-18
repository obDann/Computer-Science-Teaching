from exercise_1 import *
import unittest

class TestSquareMe(unittest.TestCase):

    def test_zero_case(self):
        actual = square_me(0.0)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_negative_case(self):
        actual = square_me(-2.0)
        expected = 4.0
        self.assertEqual(actual, expected)

    def test_n_case(self):
        actual = square_me(5.0)
        expected = 25.0
        self.assertEqual(actual, expected)

class TestKanyeHelper(unittest.TestCase):

    def test_space_case(self):
        expected = " "
        actual = kanye_helper(expected)
        self.assertEqual(actual, expected)

    def test_qm_case(self):
        input_c = "?"
        expected = "? All Day."
        actual = kanye_helper(input_c)
        self.assertEqual(actual, expected)

    def test_actual_question(self):
        input_c = "How long do y'all throw balls to the wall?"
        expected = "How long do y'all throw balls to the wall? All Day."
        actual = kanye_helper(input_c)
        self.assertEqual(actual, expected)

    def test_actual_sentence(self):
        expected = "Mermaids be comin' out of shower drains."
        actual = kanye_helper(expected)
        self.assertEqual(actual, expected)

class TestCourseMark(unittest.TestCase):

    def test_all_zeros(self):
        actual = course_mark(0, 0, 0, 0)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_perfect(self):
        actual = course_mark(10, 20, 42, 4)
        expected = 100.0
        self.assertEqual(actual, expected)

    def test_pure_calculation(self):
        expected = 78.91666666666667
        actual = course_mark(8, 17, 35, 3)
        self.assertEqual(actual, expected)

    def test_last_calculation(self):
        expected = 39.0
        actual = course_mark(5, 12, 21, 1)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)