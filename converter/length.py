"""Feature A: length conversion."""

# Number of meters in one unit.
LENGTH_UNITS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344,
}


def convert_length(value, from_unit, to_unit):
    """Convert a length value between supported units."""
    if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
        raise ValueError(f"Unsupported length unit: {from_unit!r} -> {to_unit!r}")
    if value < 0:
        raise ValueError("Length cannot be negative")
    return value * LENGTH_UNITS[from_unit] / LENGTH_UNITS[to_unit]