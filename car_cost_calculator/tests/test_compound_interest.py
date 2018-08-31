'Compound interest tests'
import numpy as np
import car_cost_calculator as ccc

def test_compound_interest_num_results():
    assert len(ccc.compound_interest(8000, 0.073, 10, 1)) == 10

def test_compound_interest():
    actual = ccc.compound_interest(8000, 0.073, 5, 1)
    expected = [8000.0, 8584.0, 9210.632, 9883.008, 10604.468]
    np.testing.assert_allclose(actual, expected, verbose=True)
    