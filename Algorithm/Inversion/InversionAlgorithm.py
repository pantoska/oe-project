import numpy as np
import Algorithm.Selection.Best as best


class InversionAlgorithm:

    def inversion(self, pop, pk):

        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        # shape[0] to ilosc rzedow, shape[1] to ilosc kolumn
        for i in range(0, pop.shape[0], 1):
            rnd = np.random.random()
            if (rnd < pk):
                first_pivot = np.random.randint(1, pop.shape[1] - 1)
                second_pivot = np.random.randint(1, pop.shape[1] - 1)

                if (first_pivot == second_pivot):
                    while (first_pivot == second_pivot):
                        second_pivot = np.random.randint(1, pop.shape[1] - 1)

                max_pivot = max(first_pivot, second_pivot)
                min_pivot = min(first_pivot, second_pivot)

                new_part = []
                for j in range(min_pivot, max_pivot):
                    new_part.append(pop[i][j])

                new_part.reverse()

                new_pop[i] = np.concatenate((pop[i][:min_pivot], new_part, pop[i][max_pivot:]))

        return new_pop

    def elite_strategy(self, pop, evaluated_pop, number=0, percent=0):

        if (percent != 0):
            b, best_value = best.Best.get_best_max(self, pop, evaluated_pop, percent)
        elif (number != 0):
            per = number / len(pop) * 100
            b, best_value = best.Best.get_best_max(self, pop, evaluated_pop, per)

        return b, best_value
