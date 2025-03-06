import unittest
from conversions import *
from conversions_refactored import convert, ConversionNotPossible

class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        test_cases = [(0, 273.15), (100, 373.15), (-273.15, 0), (25, 298.15), (300, 573.15)]
        for c, k in test_cases:
            self.assertAlmostEqual(convertCelsiusToKelvin(c), k, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [(0, 32), (100, 212), (-40, -40), (25, 77), (300, 572)]
        for c, f in test_cases:
            self.assertAlmostEqual(convertCelsiusToFahrenheit(c), f, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [(32, 0), (212, 100), (-40, -40), (77, 25), (572, 300)]
        for f, c in test_cases:
            self.assertAlmostEqual(convertFahrenheitToCelsius(f), c, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases = [(32, 273.15), (212, 373.15), (-40, 233.15), (77, 298.15), (572, 573.15)]
        for f, k in test_cases:
            self.assertAlmostEqual(convertFahrenheitToKelvin(f), k, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases = [(273.15, 0), (373.15, 100), (0, -273.15), (298.15, 25), (573.15, 300)]
        for k, c in test_cases:
            self.assertAlmostEqual(convertKelvinToCelsius(k), c, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases = [(273.15, 32), (373.15, 212), (0, -459.67), (298.15, 77), (573.15, 572)]
        for k, f in test_cases:
            self.assertAlmostEqual(convertKelvinToFahrenheit(k), f, places=2)

    def test_general_conversion(self):
        self.assertAlmostEqual(convert("Celsius", "Kelvin", 100), 373.15, places=2)
        self.assertAlmostEqual(convert("Kelvin", "Celsius", 273.15), 0, places=2)
        self.assertAlmostEqual(convert("Fahrenheit", "Celsius", 32), 0, places=2)
        self.assertAlmostEqual(convert("Miles", "Yards", 1), 1760, places=2)
        self.assertAlmostEqual(convert("Yards", "Miles", 1760), 1, places=2)
        self.assertAlmostEqual(convert("Meters", "Miles", 1609.34), 1, places=2)
        self.assertEqual(convert("Celsius", "Celsius", 100), 100)
        self.assertEqual(convert("Meters", "Meters", 500), 500)

    def test_invalid_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Miles", 100)

if __name__ == '__main__':
    unittest.main()