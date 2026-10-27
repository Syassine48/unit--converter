"""Feature B: temperature conversion."""

ABSOLUTE_ZERO_C = -273.15
SUPPORTED = ("C", "F", "K")


def _to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    return value - 273.15


def _from_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return value * 9 / 5 + 32
    return value + 273.15


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature between Celsius (C), Fahrenheit (F) and Kelvin (K)."""
    if from_unit not in SUPPORTED or to_unit not in SUPPORTED:
        raise ValueError(f"Unsupported temperature unit: {from_unit!r} -> {to_unit!r}")
    celsius = _to_celsius(value, from_unit)
    if celsius < ABSOLUTE_ZERO_C - 1e-9:
        raise ValueError("Temperature is below absolute zero")
    return _from_celsius(celsius, to_unit)
