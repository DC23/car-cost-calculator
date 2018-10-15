# -*- coding: utf-8 -*-
"Standing costs class"

from .compound_interest import compound_interest


class StandingCosts:
    """Represents static yearly costs which are not dependent on distance travelled

    Attributes:
        years (int): number of years calculated.
        inflation (float): Assumed inflation rate used for price indexing.
        insurance_cost (array-like): Inflation-indexed insurance yearly spend.
        registration_cost (array-like): Inflation-indexed registration yearly spend.
        roadside_assist_cost (array-like): Inflation-indexed roadside assistance yearly spend.
        detailing_cost (array-like): Inflation-indexed detailing and car wash yearly spend.
    """

    def __init__(
        self,
        years: int = 1,
        inflation: float = 0.02,
        insurance_per_year=500,
        registration_per_year=500,
        roadside_assist_per_year=200,
        detailing_per_year=120,
    ):
        """Initialise the standing costs object
        Args:
            years (int): number of years to model
            inflation (float): Assumed inflation rate used for price indexing.
            insurance_per_year (float): Cost of insurance in the first year.
            registration_per_year (float): Cost of registration in the first year.
            roadside_assist_per_year (float): Cost of roadside assistance in the first year.
            detailing_per_year (float): Cost of detailing and car washes in the first year.
        """
        self.years = years
        self.inflation = inflation
        self.insurance_cost = compound_interest(
            principal=insurance_per_year, annual_rate=inflation, years=years
        )
        self.registration_cost = compound_interest(
            principal=registration_per_year, annual_rate=inflation, years=years
        )
        self.roadside_assist_cost = compound_interest(
            principal=roadside_assist_per_year, annual_rate=inflation, years=years
        )
        self.detailing_cost = compound_interest(
            principal=detailing_per_year, annual_rate=inflation, years=years
        )
