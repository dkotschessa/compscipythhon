from layer import Layer
from util import sigmoid, derivative_sigmoid


def test_layer_init():
    layer_structure = [4, 6, 3]
    learning_rate = 2.0
    activation_function = sigmoid
    derivative_activation_function = derivative_sigmoid
    layer = Layer(
        None,
        layer_structure[0],
        learning_rate,
        activation_function,
        derivative_activation_function,
    )
    assert layer.previous_layer is None
    # assert layer.num_neurons == 4
    # assert layer.learning_rate == 2.0
    # assert layer.activation_function == sigmoid
    # assert layer.derivative_activation_function == derivative_sigmoid


def test_outputs():
    layer_structure = [4, 6, 3]
    learning_rate = 2.0
    activation_function = sigmoid
    derivative_activation_function = derivative_sigmoid
    layer = Layer(
        None,
        layer_structure[0],
        learning_rate,
        activation_function,
        derivative_activation_function,
    )
    layer2 = Layer(
        layer,
        layer_structure[0],
        learning_rate,
        activation_function,
        derivative_activation_function,
    )
    result = layer2.outputs([1, 2, 3])
    assert result == [0.5, 0.5, 0.5, 0.5]
