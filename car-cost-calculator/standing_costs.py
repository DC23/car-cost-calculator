'Standing costs class'

from .compound_interest import compound_interest


class StandingCosts():
    '''Represents the static costs, which are not dependent on distance travelled'''

    def __init__(self,
                 years=1,
                 cpi=0.02,
                 insurance_per_year=500,
                 registration_per_year=500,
                 roadside_assist_per_year=200):
        '''Initialise the standing costs object'''
        self.insurance_per_year = compound_interest(
            principal=insurance_per_year,
            annual_rate=cpi,
            years=years,
            compounds_per_year=1)
        self.registration_per_year = compound_interest(
            principal=registration_per_year,
            annual_rate=cpi,
            years=years,
            compounds_per_year=1)
        self.roadside_assist_per_year = compound_interest(
            principal=roadside_assist_per_year,
            annual_rate=cpi,
            years=years,
            compounds_per_year=1)
