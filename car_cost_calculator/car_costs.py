# -*- coding: utf-8 -*-
'Car cost of ownership class'

import numpy as np
import pandas as pd
from .depreciation import FlatRate
from .running_costs import RunningCosts
from .standing_costs import StandingCosts


class CarCosts():
    ''' Total cost of ownership class, encapsulating both running and standing costs.
    Adds utility functionality like pandas dataframes and plots.'''

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
                 initial_cost_per_tyre: float = 300,
                 insurance_per_year: float = 500,
                 registration_per_year: float = 500,
                 roadside_assist_per_year: float = 200,
                 detailing_per_year: float = 120):
        '''Initialise the car cost of ownership object'''
        self.running_costs = RunningCosts(
            initial_vehicle_value=initial_vehicle_value,
            initial_vehicle_age=initial_vehicle_age,
            depreciation_rate=depreciation_rate,
            years=years,
            km_per_year=km_per_year,
            litres_per_100km=litres_per_100km,
            inflation=inflation,
            initial_fuel_price=initial_fuel_price,
            initial_service_cost=initial_service_cost,
            service_interval_km=service_interval_km,
            service_interval_years=service_interval_years,
            tyre_replacement_interval=tyre_replacement_interval,
            initial_cost_per_tyre=initial_cost_per_tyre)

        self.standing_costs = StandingCosts(
            years=years,
            inflation=inflation,
            insurance_per_year=insurance_per_year,
            registration_per_year=registration_per_year,
            roadside_assist_per_year=roadside_assist_per_year,
            detailing_per_year=detailing_per_year)

    @property
    def yearly_costs(self):
        '''Gets all yearly costs as a pandas `Dataframe`'''
        pass
