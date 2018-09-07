# -*- coding: utf-8 -*-
""" Car Cost Calculator

    Total cost of ownership calculator for cars
"""

__author__ = 'DC23'
__email__ = 'jugglindan@gmail.com'
__version__ = '0.6.0'

from .car_costs import CarCosts
from .compound_interest import compound_interest
from .depreciation import FlatRate, TwoStageRate
from .running_costs import RunningCosts
from .standing_costs import StandingCosts
