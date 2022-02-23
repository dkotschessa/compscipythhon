from chromosone import Chromosone
from genetic_algorithm import GeneticAlgorithm
from random import randrange, random
from copy import deepcopy


class SimpleEquation(Chromosone):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fitness(self):
        # equation to solve
        # 6x - x^2 + 4y - y^2
        X = self.x
        Y = self.y
        # print(f"X: {X}, Y: {Y}")
        # six = 6 * X
        # x_squared = X**2
        # four_y = 4 * Y
        # y_squared = Y**2
        # print(6 * X - X**2 * 4 * Y - Y**2)
        return 6 * X - X**2 * 4 * Y - Y**2

    @classmethod
    def random_instance(cls):
        return SimpleEquation(randrange(100), randrange(100))

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        child1.y = other.y
        child2.y = self.y
        return child1, child2

    def mutate(self):
        if random() > 0.5:  # mutate x
            if random() > 0.5:
                self.x += 1
            else:
                self.x -= 1

        else:  # otherwise mutate y
            if random() > 0.5:
                self.y += 1
            else:
                self.y -= 1

    def __str__(self):
        return f"X: {self.x} Y: {self.y} Fitness: {self.fitness()}"


if __name__ == "__main__":
    initial_population = [SimpleEquation.random_instance() for _ in range(20)]

    ga = GeneticAlgorithm(
        initial_population=initial_population,
        threshold=13.0,
        max_generations=100,
        mutation_chance=0.1,
        crossover_chance=0.7,
    )
    result = ga.run()
    print(result)
