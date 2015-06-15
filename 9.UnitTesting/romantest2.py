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

    def test_too_many_repeated_input(self):
        """from_roman should fail with too many repeated numerals"""
        for s in ("MMMM","DD","CCCC","LL","XXXX","VV","IIII"):
            self.assertRaises(roman1.InvalidRomanNumeralError,roman1.from_roman,s)

    def test_repeated_pairs(self):
        """from_roman should fail with repeated pairs of numerals"""
        for s in ("CMCM","CDCD","XCXC","XLXL","IVIV"):
            self.assertRaises(roman1.InvalidRomanNumeralError,roman1.from_roman,s)

    def test_malformed_antecedents(self):
        """from_roman should fail with malformed antecedents"""
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.from_roman, s)


if __name__ == "__main__":
    unittest.main()