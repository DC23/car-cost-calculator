# -*- coding: utf-8 -*-
'Compound interest function'
import numpy as np


def compound_interest(principal: float,
                      annual_rate: float,
                      years: int,
                      compounds_per_year: int = 1):
    '''Calculates compound interest
    Solves $A = P(1+\frac{r}{n})^{nt}$ for
    P = principal
    r = annual rate
    n = number of times interest is compounded per year
    t = number of years to compound

    Args:
        principal (float): The principal (initial) value.
        annual_rate (float): The annual interest rate.
        years (int): Number of years to calculate.
        compounds_per_year (int): Number of times per year that interest is compounded.

    Returns:
        an array giving the new principal for each year in the sequence.
    '''
    return np.array([
        principal * ((1 + annual_rate / compounds_per_year)**
                     (yr * compounds_per_year)) for yr in range(years)
    ])
