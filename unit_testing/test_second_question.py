from unittest import TestCase
from second_question import *


class TestSentence(TestCase):
    def setUp(self):
        self.sentence = Sentence()

    def test_init(self):
        # Test with default text
        self.assertEqual(self.sentence.text, "Zen of Python")

        # Test with custom text
        custom_sentence = Sentence("Hello, world!")
        self.assertEqual(custom_sentence.text, "Hello, world!")

    def test_str(self):
        self.assertEqual(str(self.sentence), "Text: Zen of Python")

    def test_backwards(self):
        # Test with single word
        single_word = Sentence("Python")
        self.assertEqual(single_word.backwards(), "nohtyP")

        # Test with multiple words
        multiple_words = Sentence("Hello, world!")
        self.assertEqual(multiple_words.backwards(), "!dlrow ,olleH")

    def test_upper(self):
        # Test with lowercase letters
        lowercase_sentence = Sentence("hello, world!")
        self.assertEqual(lowercase_sentence.upper(), "HELLO, WORLD!")

        # Test with mixed case letters
        mixed_case_sentence = Sentence("HeLlo, wOrld!")
        self.assertEqual(mixed_case_sentence.upper(), "HELLO, WORLD!")

    def test_lower(self):
        # Test with uppercase letters
        uppercase_sentence = Sentence("HELLO, WORLD!")
        self.assertEqual(uppercase_sentence.lower(), "hello, world!")

        # Test with mixed case letters
        mixed_case_sentence = Sentence("HeLlo, wOrld!")
        self.assertEqual(mixed_case_sentence.lower(), "hello, world!")

    def test_search(self):
        # Test with existing word
        self.assertEqual(self.sentence.search("of"), 1)

        # Test with non-existing word
        self.assertEqual(self.sentence.search("programming"), 0)

        # Test with word occurring multiple times
        multiple_occurrences = Sentence("Hello, hello, hello!")
        self.assertEqual(multiple_occurrences.search("hello"), 3)

    def test_change(self):
        # Test with existing word
        self.assertEqual(self.sentence.change("Zen", "Hello"), "Hello of Python")

        # Test with non-existing word
        self.assertEqual(self.sentence.change("programming", "coding"), "Zen of Python")

    def test_print_word(self):
        # Test with valid index
        self.assertEqual(self.sentence.print_word(0), "Zen")

        # Test with index out of range
        self.assertEqual(self.sentence.print_word(10), None)

        # Test with negative index
        self.assertEqual(self.sentence.print_word(-1), "Python")

    def test_info(self):
        # Test with no numbers or uppercase letters
        no_numbers_or_uppercase = Sentence("zen of python")
        self.assertEqual(no_numbers_or_uppercase.info(), "Words: 3, numbers: 0, upper: 0, lower: 13")

        # Test with numbers and uppercase letters
        numbers_and_uppercase = Sentence("Hello, 123 World!")
        self.assertEqual(numbers_and_uppercase.info(), "Words: 3, numbers: 3, upper: 2, lower: 10")
