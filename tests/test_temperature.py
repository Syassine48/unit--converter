import pytest

from converter.temperature import convert_temperature


def test_celsius_to_fahrenheit_normal():
    assert convert_temperature(100, "C", "F") == pytest.approx(212)


def test_absolute_zero_boundary():
    assert convert_temperature(0, "K", "C") == pytest.approx(-273.15)


def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        convert_temperature(-300, "C", "K")
