import numpy as np


class Roulette:

    def roulette_max(self, pop, evaluated_pop, percent):
        if np.ndarray.min(evaluated_pop) <= 0:
            evaluated_pop = evaluated_pop + abs(np.ndarray.min(evaluated_pop)) + 1

        cumsum_pop = np.cumsum(evaluated_pop)
        cumsum_pop = np.insert(cumsum_pop, 0, 0)

        new_population = []
        i = 1
        counter = 0
        rand = np.random.random_sample()

        while counter < int(evaluated_pop.size * percent / 100):
            if (cumsum_pop[i - 1] / cumsum_pop[cumsum_pop.size - 1]) <= rand < (
                    cumsum_pop[i] / cumsum_pop[cumsum_pop.size - 1]):
                new_population.append(pop[i - 1])
                counter = counter + 1
                i = 1
                rand = np.random.random_sample()
            else:
                i = i + 1
        new_population = np.array(new_population)

        return new_population



    def roulette_min(self, pop, evaluated_pop, percent):
        if np.ndarray.min(evaluated_pop) <= 0:
            evaluated_pop = evaluated_pop + abs(np.ndarray.min(evaluated_pop)) + 1

        cumsum_pop = np.cumsum( 1 / evaluated_pop)
        cumsum_pop = np.insert(cumsum_pop, 0, 0)

        new_population = []
        pop_value = []
        i = 1
        counter = 0
        rand = np.random.random_sample()

        while counter < int(evaluated_pop.size * percent / 100):
            if (cumsum_pop[i - 1] / cumsum_pop[cumsum_pop.size - 1]) <= rand < (
                    cumsum_pop[i] / cumsum_pop[cumsum_pop.size - 1]):
                new_population.append(pop[i - 1])
                pop_value.append(evaluated_pop[i-1])
                counter = counter + 1
                i = 1
                rand = np.random.random_sample()
            else:
                i = i + 1
        new_population = np.array(new_population)
        pop_value = np.array(pop_value)

        return new_population, pop_value