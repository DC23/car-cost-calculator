# -*- coding: utf-8 -*-
# pylint: disable=C0103, C0111

from pytest import approx
from car_cost_calculator.depreciation import FlatRate, TwoStageRate, calculate

FLAT_RATE_15 = FlatRate(0.15)
TWO_STAGE_RATE = TwoStageRate(0.2, 0.11, 3)


def test_flat_rate():
    fr33 = FlatRate(0.33)
    for i in range(100):
        assert fr33(i) == 0.33


def test_two_stage_rate():
    tsr = TwoStageRate(0.4, 0.2, 4)
    assert tsr(0) == 0.4
    assert tsr(1) == 0.4
    assert tsr(2) == 0.4
    assert tsr(3) == 0.4
    assert tsr(4) == 0.2


def test_depreciated_value_result_sizes():
    iv = 100  # initial value
    y = 5  # num years
    ia = 0  # initial age
    dv, loss = calculate(iv, years=y, initial_age=ia, rate=FLAT_RATE_15)
    assert len(dv) == y
    assert len(loss) == y


def test_depreciated_value_first_year():
    iv = 100
    y = 5
    ia = 0  # initial age
    dv, _ = calculate(iv, years=y, initial_age=ia, rate=FLAT_RATE_15)
    assert dv[0] == approx(iv)


def test_depreciated_value_second_year():
    iv = 1000
    y = 5
    ia = 0  # initial age
    dv, _ = calculate(iv, years=y, initial_age=ia, rate=FLAT_RATE_15)
    assert dv[1] == approx(iv * (1 - FLAT_RATE_15(0)))


def test_depreciated_value():
    iv = 100
    y = 5
    ia = 0
    dv, _ = calculate(iv, years=y, initial_age=ia, rate=FLAT_RATE_15)
    r = 1 - FLAT_RATE_15(0)
    assert dv[0] == approx(iv)
    assert dv[1] == approx(dv[0] * r)
    assert dv[2] == approx(dv[1] * r)
    assert dv[3] == approx(dv[2] * r)
    assert dv[4] == approx(dv[3] * r)


def test_loss_vs_dep_value():
    iv = 100
    y = 5
    ia = 0
    dv, loss = calculate(iv, years=y, initial_age=ia, rate=TWO_STAGE_RATE)
    for i in range(y):
        assert loss[i] == approx(TWO_STAGE_RATE(i) * dv[i])


def test_cumulative_loss():
    iv = 15000
    y = 10
    ia = 0
    dv, loss = calculate(iv, years=y, initial_age=ia, rate=TWO_STAGE_RATE)
    assert dv[0] - dv[-1] == approx(loss[0:-1].sum())
