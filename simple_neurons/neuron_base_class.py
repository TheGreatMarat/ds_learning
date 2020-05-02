
from random import random


class Neuron:

    def __init__(self, neuron_id, weight=None, threshold=None):
        self.neuron_id = neuron_id
        self.threshold = threshold if threshold else round(random(), 2)
        self.weight = weight if weight else round(random(), 2)

    def activate(self, *args) -> float:
        summation = self.weight if self.threshold < sum(args) else 0.0
        return summation

    def __repr__(self):
        rep = """ Neuron: {} | Thr: {} | Wth: {} """.format(self.neuron_id, self.threshold, self.weight)
        return rep


class NegativeNeuron(Neuron):

    def __init__(self, neuron_id, weight=None):
        super().__init__(neuron_id, weight)
        self.weight = -self.weight


class CommandNeuron(Neuron):

    def __init__(self, neuron_id, vassals: list):
        super().__init__(neuron_id)
        self.vassals = vassals
        self.threshold = 0.0

    def activate(self, *args):
        summation = sum(args)

        if summation == self.threshold:
            for vassal in self.vassals:
                if isinstance(vassal, NegativeNeuron):
                    vassal.weight += 0.1
                else:
                    vassal.weight += 0.1
        else:
            return True


if __name__ == '__main__':

    input_neuron = Neuron(0, 0.6)

    inner_neuron_1 = Neuron(1)
    inner_neuron_2 = NegativeNeuron(2)

    output_neuron = Neuron(3, threshold=0.7)

    command_neuron = CommandNeuron(4, vassals=[inner_neuron_1, inner_neuron_2])

    i = 0
    while True:
        i += 1
        out = inner_neuron_2.activate(input_neuron.activate(1.1)) + inner_neuron_1.activate(input_neuron.activate(1.1))
        r = command_neuron.activate(output_neuron.activate(out))

        print()
        print()
        print("Out: ", out)
        print(inner_neuron_2)
        print(inner_neuron_1)

        if r:
            break

    print(i)