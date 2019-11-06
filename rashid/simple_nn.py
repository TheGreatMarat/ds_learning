"""
Простая нейронная сеть из книги Тарика Рашидаю.
"""

import numpy
import scipy.special


class NeuralNetwork:

    def __init__(self, input_nodes: int, hidden_nodes: int, output_nodes: int, learnig_rate: float):
        """
        Init the params.
        """

        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.learning_rate = learnig_rate

        # init weights of layers
        self.weights_inner_to_hidden = (numpy.random.rand(self.hidden_nodes, self.input_nodes) - 0.5)
        self.weights_hidden_to_output = (numpy.random.rand(self.output_nodes, self.hidden_nodes) - 0.5)

        # set activation functoin
        self.activation_function = lambda x: scipy.special.expit(x)

    def train(self):
        """
        Train network.

        :return:
        """
        pass

    def query(self, inputs_list):
        """
        Show network params.

        :return:
        """

        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.weights_inner_to_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.weights_hidden_to_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


if __name__ == "__main__":

    nn = NeuralNetwork(3, 3, 3, 0.3)
    res = nn.query([1.0, 0.5, -1.5])
    print(res)

