import numpy as np

class MutationAlgorithm:

    def mutate_one_points(self, pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(pop.shape[0]):
            random = np.random.random()
            random_index = np.random.randint(pop.shape[1] - 1)
            if random < pm:
                if pop[i][random_index] == 0:
                    new_pop[i][random_index] = 1
                else:
                    new_pop[i][random_index] = 0

        return new_pop

    def mutate_two_points(self, pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(pop.shape[0]):
            random = np.random.random()
            random_index_first = np.random.randint(pop.shape[1] - 1)
            random_index_second = np.random.randint(pop.shape[1] - 1)
            if random < pm:

                if pop[i][random_index_first] == 0:
                    new_pop[i][random_index_first] = 1
                else:
                    new_pop[i][random_index_first] = 0

                if pop[i][random_index_second] == 0:
                    new_pop[i][random_index_second] = 1
                else:
                    new_pop[i][random_index_second] = 0

        return new_pop

    def mutate_edge(self, pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(pop.shape[0]):
            random = np.random.random()
            if random < pm:
                if pop[i][pop.shape[1] - 1] == 0:
                    new_pop[i][pop.shape[1] - 1] = 1
                else:
                    new_pop[i][pop.shape[1] - 1] = 0
        return new_pop