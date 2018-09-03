# -*- coding: utf-8 -*-
'Running costs class'

import numpy as np
from .compound_interest import compound_interest
from .depreciation import FlatRate, calculate
from .fuel_costs import yearly_fuel_cost


class RunningCosts():
    '''Represents yearly running costs that depend on distance travelled'''

    def __init__(self,
                 initial_vehicle_value: float = 40000,
                 initial_vehicle_age: int = 0,
                 depreciation_rate: callable = FlatRate(),
                 years: int = 10,
                 km_per_year: float = 15000.0,
                 litres_per_100km: float = 10.0,
                 inflation: float = 0.02,
                 initial_fuel_price: float = 1.50,
                 tyre_replacement_interval=15000,
                 initial_cost_per_tyre=300):

        self.years = years
        self.km_per_year = km_per_year
        self.litres_per_100km = litres_per_100km
        self.inflation = inflation

        self.cumulative_distance = np.linspace(
            km_per_year, km_per_year * years, num=years)

        # TODO service_cost = 400,
        # TODO service_interval_km = 10000,
        # TODO service_interval_years = 1.0,

        self.depreciated_value, self.depreciation_loss = calculate(
            initial_value=initial_vehicle_value,
            years=years,
            initial_age=initial_vehicle_age,
            rate=depreciation_rate)

        self.fuel_cost = yearly_fuel_cost(
            km_per_year=km_per_year,
            litres_per_100km=litres_per_100km,
            years=years,
            inflation=inflation,
            initial_fuel_price=initial_fuel_price)

        self.indexed_cost_per_tyre = compound_interest(
            principal=initial_cost_per_tyre,
            annual_rate=inflation,
            years=years)

        self.tyre_cost = self.__calc_tyre_cost(tyre_replacement_interval)

    def __calc_tyre_cost(self, tyre_replacement_interval):
        '''Calculate tyre replacement costs'''
        # The cumulative km milestones for tyre replacement
        replacement_milestones = np.arange(tyre_replacement_interval,
                                           self.cumulative_distance[-1] + 1,
                                           tyre_replacement_interval)

        # Indicies of the year in which each replacement will fall, based on the cumulative yearly distance
        replacement_indicies = np.digitize(
            x=replacement_milestones,
            bins=self.cumulative_distance,
            right=True)

        # unique year indicices and the count of replacement events in that year
        unique_replacement_years, replacement_counts = np.unique(
            replacement_indicies, return_counts=True)

        # finally, the total cost of tyre replacements for each year,
        # assuming that 4 tyres are replaced (spares are typically longer-lasting)
        yearly_tyre_cost = np.zeros(self.years)
        for count_idx, year_idx in enumerate(unique_replacement_years):
            yearly_tyre_cost[year_idx] = replacement_counts[count_idx] * self.indexed_cost_per_tyre[year_idx] * 4
        return yearly_tyre_cost
