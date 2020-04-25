import numpy as np
from algorithm.function import Func

class Population:

    def generate_population(self, pop_size, x1_min, x1_max, x2_min, x2_max):
        population = []
        for i in range(0, pop_size):
            population.append(
                np.array([np.random.uniform(low=x1_min, high=x1_max), np.random.uniform(low=x2_min, high=x2_max)]))

        return population

    def evaluate_population(self, population):
        evaluated_pop = []
        for individual in population:
            evaluated_pop.append(Func.func(Func(), individual))

        return evaluated_pop
