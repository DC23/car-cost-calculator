# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0111

from pytest import approx
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
        litres_per_100km=9.0,
        inflation=0.02,
        initial_fuel_price=1.50,
        initial_service_cost=300,
        service_interval_km=15000,
        service_interval_years=1,
        tyre_replacement_interval=40000,
        initial_cost_per_tyre=300,
        insurance_per_year=800,
        registration_per_year=500,
        roadside_assist_per_year=120,
        detailing_per_year=15 * 12)

    yc = car_costs.yearly_costs
    assert approx(yc.insurance[0], abs=0.001) == 800.000
    assert approx(yc.registration[1], abs=0.001) == 510.000
    assert approx(yc.roadside_assist[8], abs=0.001) == 140.599
    assert approx(yc.detailing[3], abs=0.001) == 191.017
    assert approx(yc.depreciation[0], abs=0.001) == 7500.000
    assert approx(yc.fuel[5], abs=0.001) == 2235.764
    assert approx(yc.tyres[2], abs=0.001) == 1248.480
    assert approx(yc.service[3], abs=0.001) == 318.362
