# -*- coding: utf-8 -*-
'Running costs class'

from .depreciation import FlatRate, calculate
from .fuel_costs import yearly_fuel_cost


class RunningCosts():
    '''Represents yearly running costs that depend on distance travelled'''

    def __init__(self,
                 initial_vehicle_value: float,
                 initial_vehicle_age: int = 0,
                 depreciation_rate: callable = FlatRate(),
                 years: int = 10,
                 km_per_year: float = 15000.0,
                 litres_per_100km: float = 10.0,
                 inflation: float = 0.02,
                 initial_fuel_price: float = 1.50):
        # TODO tyres - cost per tyre and replacement interval (km)
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
