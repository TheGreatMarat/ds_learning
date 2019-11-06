"""
Самая простая модель фомального нейрона.

ver. 0.1
"""


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


if __name__ == '__main__':

    n1 = Neuron(1, 0.5, 0.1)
    n2 = Neuron(2, 0.1, 0.1)

    n3 = Neuron(3, 0.5, 0.6, [n1, n2])

    print(n3.activation())
