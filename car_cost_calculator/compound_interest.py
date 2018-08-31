# -*- coding: utf-8 -*-
'Compound interest function'
import numpy as np


def compound_interest(principal, annual_rate, years, compounds_per_year=1):
    'Calculates compound interest'
    return np.array([
        principal * ((1 + annual_rate / compounds_per_year)**
                     (yr * compounds_per_year)) for yr in range(years)
    ])
