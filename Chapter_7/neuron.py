from util import dot_product


class Neuron:
    def __init__(
        self,
        weights,
        learning_rate,
        activation_function,
        derivative_activation_function,
    ):
        self.weights = weights
        self.activation_function = activation_function
        self.derivative_activation_function = derivative_activation_function
        self.learning_rate = learning_rate
        self.output_cache = 0.0
        self.delta = 0.0

    def output(self, inputs):
        self.output_cache = dot_product(inputs, self.weights)
        return self.activation_function(self.output_cache)
