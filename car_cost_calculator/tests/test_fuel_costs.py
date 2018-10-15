# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0111

from numpy.testing import assert_allclose
from car_cost_calculator.fuel_costs import fuel_used, yearly_fuel_cost


def test_fuel_used_100km():
    assert fuel_used(100, 8) == 8.0


def test_fuel_used_1000km():
    assert fuel_used(1000.0, 12.2) == 122.0


def test_fuel_used_15000km():
    assert fuel_used(15000, 15.8) == 2370.0


def test_fuel_cost_over_10years():
    expected = [
        1890.0,
        1929.69,
        1970.214,
        2011.588,
        2053.831,
        2096.962,
        2140.998,
        2185.959,
        2231.864,
        2278.733,
    ]
    actual = yearly_fuel_cost(
        km_per_year=15000,
        litres_per_100km=8.4,
        years=10,
        inflation=2.1 / 100.0,
        initial_fuel_price=1.5,
    )
    assert_allclose(actual, expected, atol=0.001)
