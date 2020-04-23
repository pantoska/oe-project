import numpy as np


class Tournament:

    def tournament_max(self, pop, evaluated_pop, tournament_size):

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
        new_pop = []
        new_ev_pop = []
        for el in tour:
            best_value_in_division = max(el)
            new_pop.append(pop[np.argmax(el)])
            new_ev_pop.append(best_value_in_division)

        # return self.tournament_selection(new_pop, new_ev_pop, tournament_size)
        return new_pop, new_ev_pop


    def tournament_min(self, pop, evaluated_pop, tournament_size):

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
        new_pop = []
        new_ev_pop = []
        for el in tour:
            best_value_in_division = min(el)
            new_pop.append(pop[np.argmin(el)])
            new_ev_pop.append(best_value_in_division)

        return new_pop, new_ev_pop

