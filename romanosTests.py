import unittest

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romano_a_arabigo("I"), 1)

if __name__ == "__main__":
    unittest.main()
