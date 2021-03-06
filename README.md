# Car Cost Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

* Version: 0.6.1

An attempt at a total cost of ownership calculator, simply because I plan to get a new car and typically overthink the whole thing.

## Notebook

To run the included notebook, install the dev dependencies. They are not
included in the main dependencies as they are not strictly required for running
the package code.

```bash
pipenv install --dev
pipenv run jupyter notebook ./notebook/comparer.ipynb
```

## References

### Depreciation

1. [Dog & Lemon Guide to New Car Depreciation in Australia](https://dogandlemon.com/sites/default/files/depreciation_australia.pdf)
2. [ATO Guide to Motor Vehicle Depreciation](https://atotaxrates.info/tax-deductions/work-related-car-expenses/depreciation-of-vehicles/)
