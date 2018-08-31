# -*- coding: utf-8 -*-
'Depreciation functions'
# pylint: disable=R0903
import numpy as np


class TwoStageRate():
    '''Depreciation function with a 2-stage rate.

       Defaults to 15% for first 3 years, then 10% after that.
    '''

    def __init__(self, stage_1_rate=0.15, breakpoint=3, stage_2_rate=0.10):
        self.__stage_1_rate = stage_1_rate
        self.__breakpoint = breakpoint
        self.__stage_2_rate = stage_2_rate

    def __call__(self, year):
        if year < self.__breakpoint:
            return self.__stage_1_rate
        return self.__stage_2_rate


class FlatRate():
    '''Flat-rate depreciation function object'''

    def __init__(self, rate=0.1):
        self.__rate = rate

    def __call__(self, year):
        return self.__rate


def calc_depreciation(initial_value,
                      years=10,
                      initial_age=0,
                      dep_rate_func=FlatRate()):
    """ Calculates the yearly depreciated value for a range of years,
        given an initial value, the number of years,
        and a function that gives the depreciation rate for a given year.
        Args:
            initial_value (double): the starting value.
            years (int): the number of years to calculate.
            initial_age(int): vehicle age at start
            dep_rate_func (callable): Function accepting a single int that
                returns the depreciation rate to use for the given age in years.
        Returns:
            dep_value: numpy array containing the depreciated value for each year.
            yearly_loss: numpy array containing the depreciation loss for
                each year, defined as the difference in value between the
                start and end of the year.
    """

    dep_value = np.zeros(years)
    yearly_loss = np.zeros(years)
    dep_value[0] = initial_value
    previous = initial_value
    for year in range(1, years):
        rate = dep_rate_func(initial_age + year - 1)
        previous *= (1.0 - rate)
        dep_value[year] = previous

    for year in range(years):
        rate = dep_rate_func(initial_age + year)
        yearly_loss[year] = rate * dep_value[year]

    return dep_value, yearly_loss
