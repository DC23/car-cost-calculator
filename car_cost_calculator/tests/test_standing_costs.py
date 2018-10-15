# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0111

import numpy as np
from numpy.testing import assert_allclose
from car_cost_calculator.standing_costs import StandingCosts


def test_len_matches_years():
    years = 6
    sc = StandingCosts(years=years)
    assert len(sc.insurance_cost) == years
    assert len(sc.registration_cost) == years
    assert len(sc.roadside_assist_cost) == years


def test_standing_costs_1_year():
    actual = StandingCosts(
        years=1,
        inflation=0.02,
        insurance_per_year=100,
        registration_per_year=200,
        roadside_assist_per_year=150,
    )
    assert_allclose(100, actual.insurance_cost)
    assert_allclose(200, actual.registration_cost)
    assert_allclose(150, actual.roadside_assist_cost)
    assert_allclose(120, actual.detailing_cost)


def test_standing_costs_insurance_3_years():
    actual = StandingCosts(
        years=3,
        inflation=0.02,
        insurance_per_year=100,
        registration_per_year=200,
        roadside_assist_per_year=150,
    )
    expected = np.array([100.0, 102.0, 104.04])
    assert_allclose(expected, actual.insurance_cost)


def test_standing_costs_rego_10_years():
    actual = StandingCosts(
        years=10,
        inflation=0.02,
        insurance_per_year=100,
        registration_per_year=500,
        roadside_assist_per_year=150,
    )
    expected = np.array(
        [
            500.0,
            510.0,
            520.2,
            530.604,
            541.216,
            552.040,
            563.081,
            574.343,
            585.830,
            597.546,
        ]
    )
    assert_allclose(expected, actual.registration_cost, atol=0.001)
