# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0111

from numpy.testing import assert_allclose
from car_cost_calculator.depreciation import FlatRate, TwoStageRate
from car_cost_calculator.running_costs import RunningCosts


def test_depreciation_on_10K_over_5_years_at_11percent():
    actual = RunningCosts(
        initial_vehicle_value=10000,
        initial_vehicle_age=0,
        depreciation_rate=FlatRate(0.11),
        years=5,
    )
    expected = [10000.000, 8900.000, 7921.000, 7049.690, 6274.224]
    assert_allclose(actual.depreciated_value, expected, atol=0.001)


def test_fuel_cost():
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
    actual = RunningCosts(
        km_per_year=15000,
        litres_per_100km=8.4,
        years=10,
        inflation=2.1 / 100.0,
        initial_fuel_price=1.5,
    )
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
        initial_cost_per_tyre=1,
    )
    # One replacement event in years 2, 4 & 5
    expected = [0, 4, 0, 4, 4]
    assert_allclose(actual.tyre_cost, expected)


def test_tyres_more_than_once_per_year():
    actual = RunningCosts(
        years=3,
        inflation=0.01,
        km_per_year=10000,
        tyre_replacement_interval=3000,
        initial_cost_per_tyre=1,
    )
    # 3 replacements in first year, 3 in second, 4 in third
    expected = [12.0, 12.12, 16.3216]
    assert_allclose(actual.tyre_cost, expected)


def test_service_schedule_km_less_than_yearly():
    """Tests service interval calculations for scenario where the service
    km distance is less than the annual distance driven,
    resulting in multiple services per year"""
    actual = RunningCosts(
        years=3,
        inflation=0.0,
        km_per_year=10000.0,
        initial_service_cost=1,
        service_interval_km=3000.0,
        service_interval_years=1.0,
    )
    # 3 services in first year, 3 in second, 4 in third
    expected = [3.0, 3.0, 4.0]
    assert_allclose(actual.service_cost, expected)


def test_service_schedule_km_more_than_yearly():
    """Tests service interval calculations for scenario where the service
    km distance is more than the annual distance driven,
    resulting in the yearly service cap being applied"""
    actual = RunningCosts(
        years=5,
        inflation=0.01,
        km_per_year=10000.0,
        initial_service_cost=1,
        service_interval_km=12000.0,
        service_interval_years=1.0,
    )
    # 1 service expected each year
    expected = [1, 1.01, 1.020, 1.030, 1.040]
    assert_allclose(actual.service_cost, expected, atol=0.001)


def test_service_schedule_6_monthly_limit():
    actual = RunningCosts(
        years=5,
        inflation=0.025,
        km_per_year=10000.0,
        initial_service_cost=1,
        service_interval_km=12500.0,
        service_interval_years=0.5,
    )
    # 2 services expected each year
    expected = [2.0, 2.05, 2.101, 2.154, 2.208]
    assert_allclose(actual.service_cost, expected, atol=0.001)


def test_service_schedule_18_monthly_limit():
    actual = RunningCosts(
        years=5,
        inflation=0.0,
        km_per_year=10000.0,
        initial_service_cost=1,
        service_interval_km=20000.0,
        service_interval_years=1.5,
    )
    expected = [0, 1, 1, 0, 1]
    assert_allclose(actual.service_cost, expected, atol=0.001)


def test_total_cost():
    actual = RunningCosts(
        initial_vehicle_value=50000,
        initial_vehicle_age=0,
        depreciation_rate=TwoStageRate(
            stage_1_rate=0.15, stage_2_rate=0.1, breakpoint=3
        ),
        years=10,
        km_per_year=15000,
        litres_per_100km=16.0,
        inflation=0.02,
        initial_fuel_price=1.50,
        initial_service_cost=300,
        service_interval_km=15000,
        service_interval_years=1,
        tyre_replacement_interval=40000,
        initial_cost_per_tyre=300,
    )

    expected = [
        11400.0,
        10353.0,
        10724.79,
        7209.336,
        6985.048,
        8118.018,
        6630.519,
        7872.934,
        6382.645,
        6292.717,
    ]
    assert_allclose(actual.total_cost, expected, atol=0.001)
