import unittest
from translator import english_to_french, french_to_english

class TestEnglish2French(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('good-bye'), 'bonjour')


class TestFrench2English(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('excusez-moi'), 'thank-you')

unittest.main()