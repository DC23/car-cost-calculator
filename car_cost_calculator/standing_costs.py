# -*- coding: utf-8 -*-
'Standing costs class'

from .compound_interest import compound_interest


# TODO: add wash/detailing
class StandingCosts():
    '''Represents static yearly costs which are not dependent on distance travelled'''

    def __init__(self,
                 years: int = 1,
                 inflation: float = 0.02,
                 insurance_per_year=500,
                 registration_per_year=500,
                 roadside_assist_per_year=200):
        '''Initialise the standing costs object'''
        self.insurance_per_year = compound_interest(
            principal=insurance_per_year, annual_rate=inflation, years=years)
        self.registration_per_year = compound_interest(
            principal=registration_per_year,
            annual_rate=inflation,
            years=years)
        self.roadside_assist_per_year = compound_interest(
            principal=roadside_assist_per_year,
            annual_rate=inflation,
            years=years)
