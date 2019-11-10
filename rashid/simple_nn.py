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

    def train(self, input_list, target_list):
        """
        Train network.

        :return:
        """

        # transform input and target values into 2d array matrix
        inputs = numpy.array(input_list, ndmin=2).T
        target = numpy.array(target_list, ndmin=2).T

        # compute input signals for hidden layer
        hidden_inputs = numpy.dot(self.weights_inner_to_hidden, inputs)

        # compute output signals for hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # compute input signals for output layer
        final_inputs = numpy.dot(self.weights_hidden_to_output, hidden_outputs)

        # compute output signals for output layer
        final_output = self.activation_function(final_inputs)

        # compute network error = target values - final output values
        output_errors = target - final_output

        # compute hidden layer errors
        hidden_errors = numpy.dot(self.weights_hidden_to_output.T, output_errors)

        # update weights between hidden and output layers
        self.weights_hidden_to_output += self.learning_rate * numpy.dot((output_errors * final_output * (1.0 - final_output)),
                                                                        hidden_outputs.T)

        # update weights between input and hidden layers
        self.weights_inner_to_hidden += self.learning_rate * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs),
                                                                        inputs.T))

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

