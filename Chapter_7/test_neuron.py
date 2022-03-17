from neuron import Neuron
from util import sigmoid, derivative_sigmoid


def test_neuron_init():
    weights = [1.0, 2.0, 3.0]
    learning_rate = 1.0
    activation_function = sigmoid
    derivative_activation_function = derivative_sigmoid

    neuron = Neuron(
        weights, learning_rate, activation_function, derivative_activation_function
    )
    assert neuron.weights == weights
    assert neuron.learning_rate == learning_rate
    assert neuron.activation_function == activation_function
    assert neuron.derivative_activation_function == derivative_activation_function


def test_neuron_output():
    weights = [1.0, 2.0, 3.0]
    learning_rate = 1.0
    activation_function = sigmoid
    derivative_activation_function = derivative_sigmoid

    neuron = Neuron(
        weights, learning_rate, activation_function, derivative_activation_function
    )
    result = neuron.output([1, 1, 1])
    assert result == 0.9975273768433653
