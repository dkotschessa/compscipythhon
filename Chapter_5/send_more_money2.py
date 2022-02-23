from chromosone import Chromosone
from genetic_algorithm import GeneticAlgorithm
from random import shuffle, sample
from copy import deepcopy


class SendMoreMoney2(Chromosone):
    def __init__(self, letters):
        self.letters = letters

    def fitness(self):
        s = self.letters.index("S")
        e = self.letters.index("E")
        n = self.letters.index("N")
        d = self.letters.index("D")
        m = self.letters.index("M")
        o = self.letters.index("O")
        r = self.letters.index("R")
        y = self.letters.index("Y")
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
        difference = abs(money - (send + more))
        return 1 / (difference + 1)

    @classmethod
    def random_instance(cls):
        letters = ["S", "E", "N", "D", "M", "O", "R", "Y", " ", " "]
        shuffle(letters)
        return SendMoreMoney2(letters)

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        idx1, idx2 = sample(range(len(self.letters)), k=2)
        l1, l2 = child1.letters[idx1], child2.letters[idx2]
        child1.letters[child1.letters.index(l2)], child1.letters[idx2] = (
            child.letters[idx2],
            l2,
        )
        child2.letter[child2.letters.index(l1)], child2.letters[idx1] = (
            child2.letters[idx1],
            l1,
        )
        return child1, child2

    def mutate(self):
        idx1, idx2 = sample(range(len(letters)), k=2)
        self.letters[idx1], self.letters[idx2] = self.letters[idx2], self.letters[idx1]

    def __str__(self):
        s = self.letters.index("S")
        e = self.letters.index("E")
        n = self.letters.index("N")
        d = self.letters.index("D")
        m = self.letters.index("M")
        o = self.letters.index("O")
        r = self.letters.index("R")
        y = self.letters.index("Y")
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
        difference = abs(money - (send + more))

        return f"{send} + {more} = {money} Difference: {difference}"


if __name__ == "__main__":
    initial_population = [SendMoreMoney2.random_instance() for _ in range(1000)]
    ga = GeneticAlgorithm(
        initial_population,
        threshold=1.0,
        max_generations=1000,
        mutation_chance=0.2,
        crossover_chance=0.7,
        selection_type=GeneticAlgorithm.SelectionType.ROULETTE,
    )
    result = ga.run()
    print(result)
