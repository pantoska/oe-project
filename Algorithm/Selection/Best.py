import numpy as np


class Best:

    def get_best_max(self, pop, evaluated_pop, percent):
        copy_evaluated_pop = np.array(evaluated_pop, copy=True)

        # copy_evaluated_pop = evaluated_pop[:]
        best_individual = []
        best_value = []

        for i in range(int(evaluated_pop.size * percent / 100)):
            best = max(copy_evaluated_pop)
            best_value.append(best)

            best_individual.append(pop[np.argmax(copy_evaluated_pop)])
            copy_evaluated_pop = np.delete(copy_evaluated_pop, np.argmax(copy_evaluated_pop))

        return best_individual, best_value

    def get_best_min(self, pop, evaluated_pop, percent):
        copy_evaluated_pop = np.array(evaluated_pop, copy=True)

        # copy_evaluated_pop = evaluated_pop[:]
        best_individual = []
        best_value = []

        for i in range(int(evaluated_pop.size * percent / 100)):
            best = min(copy_evaluated_pop)
            best_value.append(best)

            best_individual.append(pop[np.argmin(copy_evaluated_pop)])
            copy_evaluated_pop = np.delete(copy_evaluated_pop, np.argmin(copy_evaluated_pop))

        return best_individual, best_value
