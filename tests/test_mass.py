import pytest

from converter.mass import convert_mass


def test_kg_to_lb_normal():
    assert convert_mass(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-4)


def test_same_unit_returns_same_value_edge_case():
    assert convert_mass(7.5, "g", "g") == pytest.approx(7.5)


def test_negative_mass_raises():
    with pytest.raises(ValueError):
        convert_mass(-1, "kg", "g")
