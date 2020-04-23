import numpy as np
import random

class Selection:

    def get_best(pop, evaluated_pop, percent, max=False, min=False):
        copy_evaluated_pop = np.array(evaluated_pop, copy=True)

        best_individual = []
        best_value = []

        for i in range(int(evaluated_pop.size * percent / 100)):
            if max:
                best = max(copy_evaluated_pop)
                best_value.append(best)

                best_individual.append(pop[np.argmax(copy_evaluated_pop)])
                copy_evaluated_pop = np.delete(copy_evaluated_pop, np.argmax(copy_evaluated_pop))
            if min:
                best = min(copy_evaluated_pop)
                best_value.append(best)

                best_individual.append(pop[np.argmin(copy_evaluated_pop)])
                copy_evaluated_pop = np.delete(copy_evaluated_pop, np.argmin(copy_evaluated_pop))

        return best_individual, best_value


    def roulette(pop, evaluated_pop, percent, max=False, min=False):

        if np.ndarray.min(evaluated_pop) < 0:
            evaluated_pop = evaluated_pop + abs(np.ndarray.min(evaluated_pop)) + 1

        distribution = []
        cumsum_pop = 0

        if max:
            cumsum_pop = np.cumsum(evaluated_pop)
            distribution.append(evaluated_pop[0]/cumsum_pop)
        if min:
            cumsum_pop = np.cumsum(1 / evaluated_pop)
            distribution.append(1/evaluated_pop[0]/cumsum_pop)

        best_individual = []

        for i in range(1, len(evaluated_pop)):
            if max:
                distribution.append((evaluated_pop[i]/cumsum_pop)+(distribution[i - 1]))
            if min:
                distribution.append((1/evaluated_pop[i]/cumsum_pop)+(distribution[i - 1]))

        for i in range(0, int(len(evaluated_pop) * percent / 100)):
            best_individual.append(pop[np.where(distribution >= np.random.random())[0][0]])

        return best_individual


    def tournament(pop, evaluated_pop, tournament_size, min=False, max=False):

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

        # selection the best from every tour
        best_individuals = []
        best_value_in_division = 0
        for el in tour:
            if max:
                best_value_in_division = max(el)
                # new_pop.append(pop[np.argmax(el)])
            if min:
                best_value_in_division = min(el)
                # new_pop.append(pop[np.argmin(el)])

            best_individuals.append(best_value_in_division)

        return best_individuals
