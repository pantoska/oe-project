import numpy as np
import random

class Selection:

    def get_best(self, pop, evaluated_pop, percent, max_func=False, min_func=False):

        copy_evaluated_pop = np.array(evaluated_pop, copy=True)

        best_individual = []
        best_value = []

        for i in range(int(len(evaluated_pop) * percent / 100)):
            if max_func:
                best = max(copy_evaluated_pop)
                best_value.append(best)

                best_individual.append(pop[np.argmax(copy_evaluated_pop)])
                copy_evaluated_pop = np.delete(copy_evaluated_pop, np.argmax(copy_evaluated_pop))
            if min_func:
                best = min(copy_evaluated_pop)
                best_value.append(best)

                best_individual.append(pop[np.argmin(copy_evaluated_pop)])
                copy_evaluated_pop = np.delete(copy_evaluated_pop, np.argmin(copy_evaluated_pop))

        return best_individual, best_value

    def roulette(self, pop, evaluated_pop, percent, max_func=False, min_func=False):

        cumsum_pop = []
        if min(evaluated_pop) <= 0:
            evaluated_pop = evaluated_pop + abs(min(evaluated_pop)) + 1

        if max_func:
            cumsum_pop = np.cumsum(evaluated_pop)
        if min_func:
            distributon = []
            for i in evaluated_pop:
                distributon.append(1 / i)
            cumsum_pop = np.cumsum(distributon)

        cumsum_pop = np.insert(cumsum_pop, 0, 0)

        new_population = []
        i = 1
        counter = 0
        rand = np.random.random_sample()

        while counter < int(len(evaluated_pop) * percent / 100):
            if (cumsum_pop[i - 1] / cumsum_pop[cumsum_pop.size - 1]) <= rand < (
                    cumsum_pop[i] / cumsum_pop[cumsum_pop.size - 1]):
                new_population.append(np.array(pop[i - 1]))
                counter = counter + 1
                i = 1
                rand = np.random.random_sample()
            else:
                i = i + 1
        return new_population

    def tournament(self, pop, evaluated_pop, tournament_size, min_func=False, max_func=False):

        copy_evaluated_pop = evaluated_pop[:]

        tour = []
        division = []
        i = 0

        while (i < tournament_size and len(copy_evaluated_pop) > tournament_size):
            select_index = np.random.randint(len(copy_evaluated_pop) - 1)
            division.append(copy_evaluated_pop[select_index])
            copy_evaluated_pop = np.delete(copy_evaluated_pop, select_index)
            i = i + 1
            if (i == tournament_size or len(copy_evaluated_pop) == tournament_size):
                tour.append(division)
                i = 0
                division = []

        if (len(copy_evaluated_pop) <= tournament_size):
            tour.append(copy_evaluated_pop)

        new_pop = []

        # selection the best from every tour
        best_individuals = []
        best_value_in_division = 0
        for el in tour:
            if max_func:
                best_value_in_division = max(el)
                new_pop.append(pop[np.argmax(el)])
            if min_func:
                best_value_in_division = min(el)
                new_pop.append(pop[np.argmin(el)])

            best_individuals.append(best_value_in_division)

        return new_pop
