from math import pi
from calculating_pi import calculate_pi



def strictly_decreasing(L):
    """
    found on https://stackoverflow.com/questions/4983258/python-how-to-check-list-monotonicity/4983359
    """
    return all(x>y for x, y in zip(L, L[1:]))


def test_converges_to_pi():
    real_pi = pi
    series = [calculate_pi(x) for x in range(100)]
    series_difference = [abs(real_pi - calculated_pi) for calculated_pi in series]
    assert strictly_decreasing(series_difference)


def test_1000000th_iteration():
    calculated_pi = calculate_pi(1000000)
    difference = abs(calculated_pi - pi)
    assert difference < .00001