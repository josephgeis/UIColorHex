import unittest
import uicolorhex


class InvalidUIColor(object):

    INVALID = 'UIColor()'


class TestNumerical(unittest.TestCase, InvalidUIColor):



    def test_numerical(self):
        test = uicolorhex.convert('#000000')
        expected = 'UIColor(red: 0/255, green: 0/255, blue: 0/255, alpha: 1.0)'
        self.assertEqual(expected, test)

    def test_alpha_lower(self):
        test = uicolorhex.convert('#abcdef')
        expected = 'UIColor(red: 171/255, green: 205/255, blue: 239/255, alpha: 1.0)'
        self.assertEqual(expected, test)

    def test_alpha_upper(self):
        test = uicolorhex.convert('#FEDCBA')
        expected = 'UIColor(red: 254/255, green: 220/255, blue: 186/255, alpha: 1.0)'
        self.assertEqual(expected, test)

    def test_alphanumeric_lower(self):
        test = uicolorhex.convert('#12ec56')
        expected = 'UIColor(red: 18/255, green: 236/255, blue: 86/255, alpha: 1.0)'
        self.assertEqual(expected, test)

    def test_numerical_with_alpha(self):
        test = uicolorhex.convert('#12121212')
        expected = 'UIColor(red: 18/255, green: 18/255, blue: 18/255, alpha: 18/255)'
        self.assertEqual(expected, test)

    def test_invalid_a(self):
        test = uicolorhex.convert('#ghijkl')
        expected = self.INVALID
        self.assertEqual(expected, test)

    def test_invalid_b(self):
        test = uicolorhex.convert('#1235')
        expected = self.INVALID
        self.assertEqual(expected, test)

    def test_invalid_c(self):
        test = uicolorhex.convert('#12345')
        expected = self.INVALID
        self.assertEqual(expected, test)

    def test_invalid_d(self):
        test = uicolorhex.convert('#1234567')
        expected = self.INVALID
        self.assertEqual(expected, test)

    def test_invalid_e(self):
        test = uicolorhex.convert('12345')
        expected = self.INVALID
        self.assertEqual(expected, test)

    def test_invalid_f(self):
        test = uicolorhex.convert('#')
        expected = self.INVALID
        self.assertEqual(expected, test)

    def test_invalid_g(self):
        test = uicolorhex.convert('#123456789')
        expected = self.INVALID
        self.assertEqual(expected, test)

    def test_strip(self):
        test = uicolorhex.convert('  #123456\n\n')
        expected = 'UIColor(red: 18/255, green: 52/255, blue: 86/255, alpha: 1.0)'
        self.assertEqual(expected, test)
