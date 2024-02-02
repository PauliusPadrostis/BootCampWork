from unittest import TestCase
from first_question import *

class Test(TestCase):
    def test_num_sum(self):
        self.assertAlmostEqual(6, num_sum(1, 2, 3))
        self.assertAlmostEqual(0, num_sum(-1, 0, 1))
        self.assertAlmostEqual(13, num_sum(10, -5, 8))
        self.assertAlmostEqual(0, num_sum(0, 0, 0))
        self.assertAlmostEqual(600, num_sum(100, 200, 300))

    def test_list_sum(self):
        self.assertAlmostEqual(6, list_sum([1, 2, 3]))
        self.assertAlmostEqual(0, list_sum([-1, 0, 1]))
        self.assertAlmostEqual(13, list_sum([10, -5, 8]))
        self.assertAlmostEqual(0, list_sum([0, 0, 0]))
        self.assertAlmostEqual(600, list_sum([100, 200, 300]))

    def test_max_num(self):
        self.assertAlmostEqual(3, max_num(1, 2, 3))
        self.assertAlmostEqual(1, max_num(-1, 0, 1))
        self.assertAlmostEqual(10, max_num(10, -5, 8))
        self.assertAlmostEqual(0, max_num(0, 0, 0))
        self.assertAlmostEqual(300, max_num(100, 200, 300))

    def test_reverse_string(self):
        self.assertEqual("olleh", reverse_string("hello"))
        self.assertEqual("nohtyp", reverse_string("python"))
        self.assertEqual("racecar", reverse_string("racecar"))
        self.assertEqual("54321", reverse_string("12345"))
        self.assertEqual("%$#@!", reverse_string("!@#$%"))

    def test_info(self):
        self.assertEqual("Upper: 2, lower: 8, numbers: 0, words: 2", info("Hello World"))
        self.assertEqual("Upper: 3, lower: 6, numbers: 0, words: 2", info("Codeium AI"))
        self.assertEqual("Upper: 0, lower: 0, numbers: 5, words: 1", info("12345"))
        self.assertEqual("Upper: 5, lower: 0, numbers: 0, words: 1", info("HELLO"))
        self.assertEqual("Upper: 0, lower: 0, numbers: 0, words: 0", info(""))

    def test_unique_only(self):
        self.assertEqual([1, 2, 3, 4, 5], unique_only(1, 2, 3, 4, 5))
        self.assertEqual([1, 2, 3], unique_only(1, 1, 2, 2, 3, 3))
        self.assertEqual([10, 20, 30, 40, 50], unique_only(10, 20, 30, 40, 50))
        self.assertEqual([100, 200, 300, 400, 500], unique_only(100, 200, 300, 400, 500))
        self.assertEqual([1, 2, 3, 4, 5], unique_only(1, 2, 3, 4, 4, 4, 5))

    def test_is_prime(self):
        self.assertTrue(True, is_prime(2))
        self.assertTrue(True, is_prime(3))
        self.assertTrue(True, is_prime(5))
        self.assertFalse(False, is_prime(4))
        self.assertFalse(False, is_prime(9))

    def test_sort_backwards(self):
        self.assertEqual("World Hello", sort_backwards("Hello World"))
        self.assertEqual("AI Codeium", sort_backwards("Codeium AI"))
        self.assertEqual("12345", sort_backwards("12345"))
        self.assertEqual("HELLO", sort_backwards("HELLO"))
        self.assertEqual("", sort_backwards(""))

    def test_is_leap(self):
        self.assertTrue(is_leap(2020))
        self.assertFalse(is_leap(2021))
        self.assertTrue(is_leap(2000))
        self.assertFalse(is_leap(1900))
        self.assertTrue(is_leap(2400))

    
