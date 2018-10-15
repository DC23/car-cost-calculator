# -*- coding: utf-8 -*-
"Compound interest function"
import numpy as np


def compound_interest(principal: float, annual_rate: float, years: int):
    """Calculates compound interest
    Solves A = P(1+r)^t for
    P = principal
    r = annual rate
    t = number of years to compound

    Args:
        principal (float): The principal (initial) value.
        annual_rate (float): The annual interest rate.
        years (int): Number of years to calculate.

    Returns:
        an array giving the new principal for each year in the sequence.
    """
    return np.array([principal * ((1 + annual_rate) ** yr) for yr in range(years)])
