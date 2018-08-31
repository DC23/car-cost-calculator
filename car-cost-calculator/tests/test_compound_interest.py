'Compound interest tests'
from .. compound_interest import compound_interest

import numpy as np

def test_compound_interest_num_results():
    assert len(compound_interest(8000, 0.073, 10, 1)) == 10

def test_compound_interest():
    actual = compound_interest(8000, 0.073, 5, 1)
    expected = [8000.0, 8584.0, 9210.632, 9883.008, 10604.468]
    np.testing.assert_allclose(actual, expected, verbose=True)
    