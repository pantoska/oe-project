from algorithm.population import Population
from algorithm.selection import Selection
from algorithm.cross import Cross
from algorithm.mutation import Mutation
from algorithm.statistics import Statistics
import numpy as np
import sys


class Algorithm:

    def run(self, x1_min, x1_max, x2_min, x2_max, generations, population_size, max, min, percent_of_best,
            best_selection, roulette_selection, tournament_selection,
            tournament_size, cross_probability, cross_points, uniform_cross,arithmetic_cross,heuristic_cross, mutation_probability,
            edge_mutation, mutation_points, mutate_change_index, mutate_even):

        import time

        statistics = []
        current_best_value = 0
        current_best_value_max = 0
        best_individuals = []
        current_best_value_min = sys.maxsize

        start_time = time.time()

        population = Population.generate_population(Population(), population_size, x1_min, x1_max, x2_min, x2_max )

        for i in range(0, generations):

            evaluated_pop = Population.evaluate_population(Population(), population)
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
            elif (arithmetic_cross):
                new_pop = Cross.arithmetic_cross(Cross(), best_individuals, cross_probability)
            elif (heuristic_cross):
                new_pop = Cross.heuristic_cross(Cross(), best_individuals, cross_probability)
            else:
                new_pop = Cross.cross(Cross(), best_individuals, population_size, cross_probability, cross_points)

            if (edge_mutation):
                population = Mutation.mutate_edge(Mutation(), new_pop, mutation_probability)
            elif mutate_change_index:
                population = Mutation.mutate_change_index(Mutation(), new_pop, mutation_probability)
            elif mutate_even:
                population = Mutation.mutate_even(Mutation(), new_pop, mutation_probability, x1_min, x1_max, x2_min, x2_max)
            else:
                population = Mutation.mutate(Mutation(), new_pop, mutation_probability, mutation_points)

            if max:
                if np.max(Population.evaluate_population(Population(), population)) > current_best_value_max:
                    best_gen = Population.evaluate_population(Population(), population)
                    current_best_value = np.max(best_gen)
            else:
                if np.min(Population.evaluate_population(Population(), population)) < current_best_value_min:
                    best_gen = Population.evaluate_population(Population(), population)
                    current_best_value = np.min(best_gen)

        stop_time = time.time()
        time = abs(stop_time - start_time)

        values, std_devs, min_values, max_values, avg_values, gen, index_min, index_max = Statistics.generate_stats(Statistics(), statistics)

        return current_best_value, time, values, std_devs, min_values, max_values, avg_values, gen, index_min, index_max
