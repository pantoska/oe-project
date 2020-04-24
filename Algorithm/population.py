import numpy as np
from Algorithm.chromosome import Chromosome
from Algorithm.function import Func


class Population:

    #generate population
    def generate_population(self, amount_individuals, amount_bits):
        population = np.random.randint(2, size=(amount_individuals, amount_bits))
        return population

    # calculate function on every individual
    def evaluate_population(self, population, x1_bits, x2_bits, x1_min, x2_min, x1_step, x2_step):
        evaluated_pop = []
        for i in population:
            individual = Chromosome.decode_individual(Population(), i, x1_bits, x2_bits, x1_min, x2_min, x1_step, x2_step)
            evaluated_pop.append(Func.func(Func(), individual))
        return evaluated_pop