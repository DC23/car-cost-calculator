# -*- coding: utf-8 -*-
'Running costs class'

import numpy as np
from .compound_interest import compound_interest
from .depreciation import FlatRate, calculate
from .fuel_costs import yearly_fuel_cost


class RunningCosts():
    '''Represents yearly running costs that depend on distance travelled.

    Attributes:
        years (int): number of years calculated.
        km_per_year (float): km driven per year.
        litres_per_100km (float): fuel consumption.
        inflation (float): Assumed inflation rate used for price indexing.
        cumulative_distance (array-like): Array giving the accumulated distance driven each year.
        depreciated_value (array-like): Array giving the depreciated value at the start of each year.
        depreciation_loss (array-like): The depreciation loss for each year.
        fuel_cost (array-like): Yearly fuel spend, based on distance driven, fuel consumption and indexed fuel cost.
        tyre_cost (array-like): Yearly spend on replacement tyres.
        service_cost (array-like): Yearly spend on servicing
        indexed_cost_per_tyre (array-like): Indexed cost of replacement tyres.
        indexed_service_cost (array-like): Indexed cost of servicing for each year.
    '''

    def __init__(self,
                 initial_vehicle_value: float = 40000,
                 initial_vehicle_age: int = 0,
                 depreciation_rate: callable = FlatRate(),
                 years: int = 10,
                 km_per_year: float = 15000.0,
                 litres_per_100km: float = 10.0,
                 inflation: float = 0.02,
                 initial_fuel_price: float = 1.50,
                 initial_service_cost: float = 400.0,
                 service_interval_km: float = 15000.0,
                 service_interval_years: float = 1.0,
                 tyre_replacement_interval: float = 15000,
                 initial_cost_per_tyre: float = 300):
        ''' Initialisation of the `RunningCosts` class.
        Args:
            initial_vehicle_value (float): Vehicle value at start of first year.
            initial_vehicle_age (int): Age of vehicle at start of first modelling year.
            depreciation_rate (callable): Function returning the depreciation rate for a given year.
            years (int): number of years to model.
            km_per_year (float): km driven per year.
            litres_per_100km (float): fuel consumption.
            inflation (float): Assumed inflation rate used for price indexing.
            initial_fuel_price (float): Price per litre of fuel in the first year. Indexed by inflation.
            initial_service_cost (float): Price per service at start of modelling period. Indexed by inflation.
            service_interval_km (float): Max distance between services.
            service_interval_years (float): Max time in years between services.
            tyre_replacement_interval (float): Interval in km between tyre replacements.
            initial_cost_per_tyre (float): Indexed replacement cost of a tyre at start of modelling period.
        '''
        assert inflation >= 0
        assert inflation <= 1.0

        self.years = years
        self.km_per_year = km_per_year
        self.litres_per_100km = litres_per_100km
        self.inflation = inflation

        self.cumulative_distance = np.linspace(
            km_per_year, km_per_year * years, num=years)

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

        # assuming that 4 tyres are replaced (spares are typically longer-lasting)
        self.indexed_cost_per_tyre = compound_interest(
            principal=initial_cost_per_tyre * 4,
            annual_rate=inflation,
            years=years)

        self.tyre_cost = self.__calc_distance_interval_costs(
            tyre_replacement_interval, self.indexed_cost_per_tyre,
            self.cumulative_distance)

        self.indexed_service_cost = compound_interest(
            principal=initial_service_cost, annual_rate=inflation, years=years)

        self.service_cost = self.__calc_service_cost(service_interval_km,
                                                     service_interval_years)

    def __calc_service_cost(self, service_interval_km, service_interval_years):
        '''Calculate cost of services that are based on both a distance and time interval'''

        # if service interval in km is less than distance travelled in min service interval years,
        # then the service interval is calculated in the same manner as tyre replacements
        if service_interval_km <= self.km_per_year * service_interval_years:
            return self.__calc_distance_interval_costs(
                service_interval_km, self.indexed_service_cost,
                self.cumulative_distance)

        # interservice distance is more than service interval time,
        # so we hit the time-based service interval instead
        return self.__calc_distance_interval_costs(
            service_interval_years, self.indexed_service_cost,
            np.array(range(1, self.years + 1)))

    def __calc_distance_interval_costs(self, replacement_interval,
                                       yearly_indexed_cost,
                                       cumulative_distance):
        '''Calculate replacement costs that are based on fixed distance intervals'''
        # The cumulative km milestones for tyre replacement
        replacement_milestones = np.arange(replacement_interval,
                                           cumulative_distance[-1] + 1,
                                           replacement_interval)

        # Indicies of the year in which each replacement will fall, based on the cumulative yearly distance
        replacement_indicies = np.digitize(
            x=replacement_milestones, bins=cumulative_distance, right=True)

        # unique year indicices and the count of replacement events in that year
        unique_replacement_years, replacement_counts = np.unique(
            replacement_indicies, return_counts=True)

        # finally, the total yearly cost
        yearly_cost = np.zeros(self.years)
        for count_idx, year_idx in enumerate(unique_replacement_years):
            try:
                yearly_cost[
                    year_idx] = replacement_counts[count_idx] * yearly_indexed_cost[year_idx]
            except IndexError:
                continue
        return yearly_cost

    @property
    def total_cost(self):
        '''Gets the total yearly spend'''
        return self.depreciation_loss + self.fuel_cost + self.tyre_cost + self.service_cost
