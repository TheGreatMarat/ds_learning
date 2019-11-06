"""
Самая простая модель фомального нейрона.

ver. 0.1
"""

import random


class Neuron:

    def __init__(self, neuron_id: int, initial_weight: float, threshold: float, initial_dendrites=[]):

        self.__id = neuron_id
        self.__dendrites = initial_dendrites
        self.__weight = initial_weight
        self.__threshold = threshold

    def summation(self):

        summation_result = 0.0

        for neuron in self.__dendrites:
            summation_result += neuron.fire()

        return summation_result

    def activation(self):
        return self.fire() if self.summation() >= self.__threshold else 0.0

    def fire(self):
        return self.__weight

    def get_neuron_id(self):
        return self.__id

    def set_dendrites(self, neurons: list):
        self.__dendrites = neurons

    def get_neuron_info(self):
        return self.__id, self.__weight, self.__threshold


class Pool:

    def __init__(self, input_count: int, inner_count: int, output_count: int):
        self.input_count = input_count
        self.inner_count = inner_count
        self.output_count = output_count

        self.input_layer = None
        self.inner_layer = None
        self.output_layer = None

    def __create_input_layer(self):
        input_layer = []
        for i in range(self.input_count):
            input_layer.append(Neuron(i, random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)))

        return input_layer

    def __create_inner_layer(self):

        inner_layer = []

        for i in range(self.input_count, self.input_count + self.inner_count):
            inner_layer.append(Neuron(i, random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)))

        return inner_layer

    def __create_output_layer(self):

        output_layer = []

        for i in range(self.input_count + self.inner_count, self.output_count + self.input_count + self.inner_count):
            output_layer.append(Neuron(i, random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)))

        return output_layer

    def connect(self):

        self.input_layer = self.__create_input_layer()
        self.inner_layer = self.__create_inner_layer()
        self.output_layer = self.__create_output_layer()

        # print('first neuron is', self.input_layer[0].get_neuron_id())
        # print('last neuron in input is', self.input_layer[-1].get_neuron_id())
        # print()
        # print('first neuron in inner is', self.inner_layer[0].get_neuron_id())
        # print('last neuron in inner is', self.inner_layer[-1].get_neuron_id())
        # print()
        # print('first neuron in output is', self.output_layer[0].get_neuron_id())
        # print('last neuron in output is', self.output_layer[-1].get_neuron_id())

        for neuron in self.inner_layer:
            neuron.set_dendrites(self.input_layer)

        for neuron in self.output_layer:
            neuron.set_dendrites(self.input_layer)

    def step(self):
        for neuron in self.output_layer:
            print(neuron.activation())

    def show_weights(self, layer: str):

        print("Weights of", layer)

        for neuron in self.__getattribute__(layer):
            print(neuron.get_neuron_info())


if __name__ == '__main__':

    n1 = Neuron(1, 0.5, 0.1)
    n2 = Neuron(2, 0.1, 0.1)

    n3 = Neuron(3, 0.5, 0.6, [n1, n2])

    print(n3.activation())

    # for i in range(5):
    #     print()
    p = Pool(2, 4, 2)
    p.connect()
    p.step()

    p.show_weights('inner_layer')
    p.show_weights('output_layer')