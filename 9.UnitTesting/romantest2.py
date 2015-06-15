__author__ = 'PyBeaner'
import unittest,roman1

#  good-input testcases should be separate with the bad ones
class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        """to_roman should fail with large input"""
        self.assertRaises(roman1.OutOfRangeError,roman1.to_roman,4000)

    def test_zero(self):
        """to_roman should fail with 0 input"""
        self.assertRaises(roman1.OutOfRangeError,roman1.to_roman,0)

    def test_negative(self):
        """to_roman should fail with negative input"""
        self.assertRaises(roman1.OutOfRangeError,roman1.to_roman,-1)

    def test_not_integer(self):
        """to_roman should fail with non-integer input"""
        self.assertRaises(roman1.NotIntegerError,roman1.to_roman,0.5)


if __name__ == "__main__":
    unittest.main()