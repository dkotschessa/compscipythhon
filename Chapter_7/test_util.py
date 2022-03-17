from util import dot_product, sigmoid, derivative_sigmoid


def test_dot_product():
    result = dot_product([1, 1], [2, 2])
    assert result == 4


def test_sigmoid():
    result = sigmoid(1)
    assert result == 0.7310585786300049


def test_derivative_sigmoid():
    result = derivative_sigmoid(1)
    assert result == 0.19661193324148185
