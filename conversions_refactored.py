class ConversionNotPossible(Exception):
    """Custom exception for invalid conversions"""
    pass

def convert(fromUnit, toUnit, value):
    temperature_units = {"Celsius", "Fahrenheit", "Kelvin"}
    distance_units = {"Miles", "Yards", "Meters"}

    if fromUnit in temperature_units and toUnit in temperature_units:
        conversions = {
            ("Celsius", "Kelvin"): lambda x: x + 273.15,
            ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
            ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
            ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
            ("Kelvin", "Celsius"): lambda x: x - 273.15,
            ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
        }
        return conversions.get((fromUnit, toUnit), lambda x: x)(value)

    elif fromUnit in distance_units and toUnit in distance_units:
        conversion_factors = {
            ("Miles", "Yards"): 1760,
            ("Miles", "Meters"): 1609.34,
            ("Yards", "Miles"): 1/1760,
            ("Yards", "Meters"): 0.9144,
            ("Meters", "Miles"): 1/1609.34,
            ("Meters", "Yards"): 1.09361,
        }
        return value * conversion_factors.get((fromUnit, toUnit), 1)

    raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")