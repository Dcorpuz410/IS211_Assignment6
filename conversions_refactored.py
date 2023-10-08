class ConversionNotPossible(Exception):
    pass


myDict = {
    # temperatures
    ("celsius", "kelvin"): "value + 273.15",
    ("celsius", "fahrenheit"): "(value * (9/5)) + 32",
    ("fahrenheit", "celsius"): "(value - 32) * (5/9)",
    ("fahrenheit", "kelvin"): "(value + 459.67) * (5/9)",
    ("kelvin", "celsius"): "value - 273.15",
    ("kelvin", "fahrenheit"): "(value * (9/5)) - 459.67",
    # distance
    ("miles", "yards"): "value * 1760",
    ("miles", "meters"): "value * 1609.344",
    ("yards", "miles"): "value / 1760",
    ("yards", "meters"): "value * 0.9144",
    ("meters", "yards"): "value / 0.9144",
    ("meters", "miles"): "value / 1609.344"
        }

unitTypes = {
    "miles": "distance",
    "meters": "distance",
    "yards": "distance",
    "celsius": "temperature",
    "fahrenheit": "temperature",
    "kelvin": "temperature"
    }


def convert(fromUnit, toUnit, value):
    # converting incompatible units
    if unitTypes.get(fromUnit) != unitTypes.get(toUnit):
        raise ConversionNotPossible
    # converting to itself
    elif fromUnit == toUnit:
        return value
    else:
        return round(eval(myDict[(fromUnit, toUnit)]), 2)