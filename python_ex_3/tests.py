import unittest

from answer import roman_to_int


class LotteryTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(roman_to_int('I'), 1)

    def test_4(self):
        self.assertEqual(roman_to_int('IV'), 4)

    def test_21(self):
        self.assertEqual(roman_to_int('XXI'), 21)

    def test_222(self):
        self.assertEqual(roman_to_int('CCXXII'), 222)

    def test_1904(self):
        self.assertEqual(roman_to_int('MCMIV'), 1904)


if __name__ == '__main__':
    unittest.main()
