# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0111

from numpy.testing import assert_allclose
from car_cost_calculator.car_costs import CarCosts
from car_cost_calculator.depreciation import TwoStageRate


def test_yearly_costs():
    car_costs = CarCosts(
        initial_vehicle_value=50000,
        initial_vehicle_age=0,
        depreciation_rate=TwoStageRate(
            stage_1_rate=0.15, stage_2_rate=0.1, breakpoint=3),
        years=10,
        km_per_year=15000,
        litres_per_100km=16.0,
        inflation=0.02,
        initial_fuel_price=1.50,
        initial_service_cost=300,
        service_interval_km=15000,
        service_interval_years=1,
        tyre_replacement_interval=40000,
        initial_cost_per_tyre=300)

    yc = car_costs.yearly_costs
    