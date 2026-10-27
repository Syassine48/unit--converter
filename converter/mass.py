"""Feature C: mass conversion."""

# Number of grams in one unit.
MASS_UNITS = {
    "mg": 0.001,
    "g": 1.0,
    "kg": 1000.0,
    "oz": 28.349523125,
    "lb": 453.59237,
}


def convert_mass(value, from_unit, to_unit):
    """Convert a mass value between supported units."""
    if from_unit not in MASS_UNITS or to_unit not in MASS_UNITS:
        raise ValueError(f"Unsupported mass unit: {from_unit!r} -> {to_unit!r}")
    if value < 0:
        raise ValueError("Mass cannot be negative")
    return value * MASS_UNITS[from_unit] / MASS_UNITS[to_unit]
