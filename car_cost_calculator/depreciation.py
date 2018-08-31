# -*- coding: utf-8 -*-
'Depreciation functions'
# pylint: disable=R0903
import numpy as np


class TwoStageRate():
    '''Depreciation rate function with a 2-stage rate.

       Defaults to 15% for first 3 years, then 10% after that.
    '''

    def __init__(self,
                 stage_1_rate: float = 0.15,
                 stage_2_rate: float = 0.10,
                 breakpoint: int = 3):
        self.__stage_1_rate = stage_1_rate
        self.__stage_2_rate = stage_2_rate
        self.__breakpoint = breakpoint

    def __call__(self, year):
        if year < self.__breakpoint:
            return self.__stage_1_rate
        return self.__stage_2_rate


class FlatRate():
    '''Flat-rate depreciation rate function object'''

    def __init__(self, rate: float = 0.1):
        self.__rate = rate

    def __call__(self, year: int):
        return self.__rate


def calculate(initial_value: float,
              years: int = 10,
              initial_age: int = 0,
              rate: callable = FlatRate()):
    """ Calculates the yearly depreciated value for a range of years,
        given an initial value, the number of years,
        and a function that gives the depreciation rate for a given year.
        Args:
            initial_value (double): the starting value.
            years (int): the number of years to calculate.
            initial_age(int): vehicle age at start
            rate (callable): Function accepting a single int that
                returns the depreciation rate to use for the given age in years.
        Returns:
            dep_value: numpy array containing the depreciated value at the start of each year.
            yearly_loss: numpy array containing the depreciation loss for
                each year, defined as the difference in value between the
                start and end of the year.
    """

    dep_value = np.zeros(years)
    yearly_loss = np.zeros(years)
    dep_value[0] = initial_value
    previous = initial_value
    for year in range(1, years):
        this_years_rate = rate(initial_age + year - 1)
        previous *= (1.0 - this_years_rate)
        dep_value[year] = previous

    for year in range(years):
        this_years_rate = rate(initial_age + year)
        yearly_loss[year] = this_years_rate * dep_value[year]

    return dep_value, yearly_loss
