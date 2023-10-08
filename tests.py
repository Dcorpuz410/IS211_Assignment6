import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()import conversions
import unittest


class KnownValues(unittest.TestCase):
    # Values stored as Celsius / Fahrenheit / Kelvin
    MyValuesCFK = (
        (-5.0, 23.0, 268.15),
        (-1, 30.2, 272.15),
        (0.0, 32.0, 273.15),
        (5.0, 41.0, 278.15),
        (2356.85, 4274.33, 2630.0)
    )

    # celsius
    def test_convertCelsiusToKelvin(self):
        print("Tests Celsius to kelvin conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            kelvin_compare = i[2]
            print("Testing", str(celsius_val) + "c,", str(kelvin_compare) + "k")
            kelvin = conversions.convertCelsiusToKelvin(celsius_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertCelsiusToFahrenheit(self):
        print("Tests Celsius to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            celsius_val = i[0]
            fahrenheit_compare = i[1]
            print("Testing", str(celsius_val) + "c,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertCelsiusToFahrenheit(celsius_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

        # fahrenheit

    def test_convertFahrenheitToKelvin(self):
        print("Tests Fahrenheit to kelvin conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            kelvin_compare = i[2]
            print("Testing", str(fahrenheit_val) + "f,", str(kelvin_compare) + "k")
            kelvin = conversions.convertFahrenheitToKelvin(fahrenheit_val)
            self.assertEqual(kelvin_compare, kelvin, "Sorry: values do not match")

    def test_convertFahrenheitToCelsius(self):
        print("Tests Fahrenheit to Celsius conversion:")
        for i in self.MyValuesCFK:
            fahrenheit_val = i[1]
            celsius_compare = i[0]
            print("Testing", str(fahrenheit_val) + "f,", str(celsius_compare) + "c")
            celsius = conversions.convertFahrenheitToCelsius(fahrenheit_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")

    # kelvin
    def test_convertKelvinToFahrenheit(self):
        print("Tests kelvin to Fahrenheit conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            fahrenheit_compare = i[1]
            print("Testing", str(kelvin_val) + "k,", str(fahrenheit_compare) + "f")
            fahrenheit = conversions.convertKelvinToFahrenheit(kelvin_val)
            self.assertEqual(fahrenheit_compare, fahrenheit, "Sorry: values do not match")

    def test_convertKelvinToCelsius(self):
        print("Tests kelvin to Celsius conversion:")
        for i in self.MyValuesCFK:
            kelvin_val = i[2]
            celsius_compare = i[0]
            print("Testing", str(kelvin_val) + "k,", str(celsius_compare) + "f")
            celsius = conversions.convertKelvinToCelsius(kelvin_val)
            self.assertEqual(celsius_compare, celsius, "Sorry: values do not match")


if __name__ == '__main__':
    unittest.main()