from algorithm.chromosome import Chromosome
from algorithm.population import Population
from algorithm.selection import Selection
from algorithm.cross import Cross
from algorithm.mutation import Mutation
from algorithm.inversion import Inversion
from algorithm.statistics import Statistics
import numpy as np
import sys


class Algorithm:

    def run(self, x1_min, x1_max, x2_min, x2_max, generations, population_size, precision, max, min, percent_of_best,
            best_selection, roulette_selection, tournament_selection,
            tournament_size, cross_probability, cross_points, uniform_cross, mutation_probability,
            edge_mutation, mutation_points, inversion_probability):

        import time

        statistics = []
        current_best_value = 0
        current_best_value_max = 0
        best_individuals = []
        current_best_value_min = sys.maxsize

        start_time = time.time()

        x1_bits, x1_dx = Chromosome.get_amount_bits(Chromosome(), x1_min, x1_max, precision)
        x2_bits, x2_dx = Chromosome.get_amount_bits(Chromosome(), x2_min, x2_max, precision)

        population = Population.generate_population(Population(), population_size, x1_bits + x2_bits)

        for i in range(0, generations):

            evaluated_pop = Population.evaluate_population(Population(), population, x1_bits, x2_bits, x1_min, x2_min,
                                                           x1_dx, x2_dx)
            statistics.append(evaluated_pop)

            if best_selection:
                best_individuals, best_value = Selection.get_best(Selection(), population, evaluated_pop,
                                                                  percent_of_best, max, min)
            elif roulette_selection:
                best_individuals = Selection.roulette(Selection(), population, evaluated_pop, percent_of_best, max, min)
            elif tournament_selection:
                best_individuals = Selection.tournament(Selection(), population, evaluated_pop, tournament_size, min,
                                                        max)

            if (uniform_cross):
                new_pop = Cross.uniform_cross(Cross(), best_individuals, population_size, cross_probability)
            else:
                new_pop = Cross.cross(Cross(), best_individuals, population_size, cross_probability, cross_points)

            if (edge_mutation):
                new_pop_mut = Mutation.mutate_edge(Mutation(), new_pop, mutation_probability)
            else:
                new_pop_mut = Mutation.mutate(Mutation(), new_pop, mutation_probability, mutation_points)

            population = Inversion.inversion(Inversion(), new_pop_mut, inversion_probability)

            if max:
                if np.max(Population.evaluate_population(Population(), population, x1_bits, x2_bits, x1_min, x2_min,
                                                         x1_dx, x2_dx)) > current_best_value_max:
                    best_gen = Population.evaluate_population(Population(), population, x1_bits, x2_bits, x1_min,
                                                              x2_min,
                                                              x1_dx, x2_dx)

                    current_best_value = np.max(best_gen)
            else:
                if np.min(Population.evaluate_population(Population(), population, x1_bits, x2_bits, x1_min, x2_min,
                                                         x1_dx, x2_dx)) < current_best_value_min:
                    best_gen = Population.evaluate_population(Population(), population, x1_bits, x2_bits, x1_min,
                                                              x2_min,
                                                              x1_dx, x2_dx)

                    current_best_value = np.min(best_gen)

        stop_time = time.time()
        time = abs(stop_time - start_time)

        values, std_devs, min_values, max_values, avg_values, gen, index_min, index_max = Statistics.generate_stats(Statistics(), statistics)

        return current_best_value, time, values, std_devs, min_values, max_values, avg_values, gen, index_min, index_max
