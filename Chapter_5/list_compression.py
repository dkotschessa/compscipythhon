from chromosone import Chromosone
from genetic_algorithm import GeneticAlgorithm
from random import shuffle, sample
from copy import deepcopy
from zlib import compress
from sys import getsizeof
from pickle import dumps


PEOPLE = [
    "Michael",
    "Sarah",
    "Joshua",
    "Narine",
    "David",
    "Sajid",
    "Melanie",
    "Daniel",
    "Wei",
    "Dean",
    "Brian",
    "Murat",
    "Lisa",
]


class ListCompresion(Chromosone):
    def __init__(self, lst):
        self.lst = lst

    @property
    def bytes_compressed(self):
        pickled_list = dumps(self.lst)
        compressed_pickled_list = compress(pickled_list)
        return getsizeof(compressed_pickled_list)

    def fitness(self):
        return 1 / self.bytes_compressed

    @classmethod
    def random_instance(cls):
        mylst = deepcopy(PEOPLE)
        shuffle(mylst)
        return ListCompresion(mylst)

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        list_length = len(self.lst)
        list_range = range(list_length)

        idx1, idx2 = sample(list_range, k=2)
        l1, l2 = child1.lst[idx1], child2.lst[idx2]
        child1_index = child1.lst.index(l2)
        child2_index = child2.lst.index(l1)
        child1.lst[child1_index], child1.lst[idx2] = child1.lst[idx2], l2
        child2.lst[child2_index], child2.lst[idx1] = child2.lst[idx1], l1
        return child1, child2

    def mutate(self):
        list_length = len(self.lst)
        idx1, idx2 = sample(range(list_length), k=2)
        self.lst[idx1], self.lst[idx2] = self.lst[idx2], self.lst[idx1]

    def __str__(self):
        return f"Order: {self.lst} Bytes: {self.bytes_compressed}"


if __name__ == "__main__":
    initial_population = [ListCompresion.random_instance() for _ in range(1000)]
    ga = GeneticAlgorithm(
        initial_population,
        threshold=1.0,
        max_generations=1000,
        mutation_chance=0.2,
        crossover_chance=0.7,
        selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT,
    )
    result = ga.run()
    print(result)
