# -*- coding: utf-8 -*-
'fuel cost functions'
# pylint: disable=R0903
from .compound_interest import compound_interest


def fuel_used(distance_km: float, litres_per_100km: float):
    '''
    Calculates the amount of fuel used for a given number of kilometers and fuel efficiency.

    Args:
        distance_km (float): Distance driven in km.
        litres_per_100km (float): Fuel efficiency in litres per 100km.

    Returns:
        float: quantity of fuel used.
    '''
    return distance_km * litres_per_100km / 100.0


def yearly_fuel_cost(km_per_year, litres_per_100km: float, years: int,
                     inflation: float, initial_fuel_price: float):
    '''
    Calculates the yearly indexed fuel cost based on an inflation rate,
    initial fuel cost, and number of km driven per year.

    Args:
        km_per_year: Distance in kilometres driven per year.
        litres_per_100km (float): Fuel efficiency in litres per 100km.
        years (int): Number of years to calculate.
        inflation (float): Inflation rate of fuel price.
        initial_fuel_price (float): Initial fuel price in dollars per litre.

    Returns:
        numpy.array: Yearly total fuel cost.
    '''
    assert inflation >= 0
    assert inflation <= 1.0

    fuel_used_per_year = fuel_used(km_per_year, litres_per_100km)
    indexed_fuel_cost_per_litre = compound_interest(
        principal=initial_fuel_price,
        annual_rate=inflation,
        years=years)
    return indexed_fuel_cost_per_litre * fuel_used_per_year
