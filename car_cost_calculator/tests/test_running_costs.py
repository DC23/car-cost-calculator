# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0111

# import numpy as np
from numpy.testing import assert_allclose
from car_cost_calculator.depreciation import FlatRate
from car_cost_calculator.running_costs import RunningCosts


def test_depreciation_on_10K_over_5_years_at_11percent():
    actual = RunningCosts(
        initial_vehicle_value=10000,
        initial_vehicle_age=0,
        depreciation_rate=FlatRate(0.11),
        years=5)
    expected = [10000.000, 8900.000, 7921.000, 7049.690, 6274.224]
    assert_allclose(actual.depreciated_value, expected, atol=0.001)

def test_fuel_cost():
    expected = [
        1890.0, 1929.69, 1970.214, 2011.588, 2053.831, 2096.962, 2140.998,
        2185.959, 2231.864, 2278.733
    ]
    actual = RunningCosts(
        km_per_year=15000,
        litres_per_100km=8.4,
        years=10,
        inflation=2.1 / 100.0,
        initial_fuel_price=1.5)
    assert_allclose(actual.fuel_cost, expected, atol=0.001)

def test_cumulative_distance():
    actual = RunningCosts(years=5, km_per_year=1000)
    expected = [1000, 2000, 3000, 4000, 5000]
    assert_allclose(actual.cumulative_distance, expected)

def test_tyre_replacement_schedule():
    actual = RunningCosts(
        years=5,
        inflation=0.0,
        km_per_year=10000,
        tyre_replacement_interval=16000,
        initial_cost_per_tyre=1)
    # One replacement event in years 2, 4 & 5
    expected = [0, 4, 0, 4, 4]
    assert_allclose(actual.tyre_cost, expected)

def test_tyres_more_than_once_per_year():
    actual = RunningCosts(
        years=3,
        inflation=0.01,
        km_per_year=10000,
        tyre_replacement_interval=3000,
        initial_cost_per_tyre=1)
    # 3 replacements in first year, 3 in second, 4 in third
    expected = [12.0, 12.12, 16.3216]
    assert_allclose(actual.tyre_cost, expected)
