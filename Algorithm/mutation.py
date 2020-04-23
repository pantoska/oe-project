import numpy as np

class Mutation:

    def mutate(pop, pm, points):
        new_pop = np.array(pop, copy=True)
        for i in range(len(pop)):
            random = np.random.random()
            random_index_first = np.random.randint(len(pop[0]))

            if points == 2:
                random_index_second = np.random.randint(len(pop[0]))

            if random < pm:
                if pop[i][random_index_first] == 0:
                    new_pop[i][random_index_first] = 1
                else:
                    new_pop[i][random_index_first] = 0

                if points == 2:
                    if pop[i][random_index_second] == 0:
                        new_pop[i][random_index_second] = 1
                    else:
                        new_pop[i][random_index_second] = 0

        return np.array(new_pop)

    def mutate_edge(pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(len(pop)):
            random = np.random.random()
            if random < pm:
                if pop[i][len(pop[0]) - 1] == 0:
                    new_pop[i][len(pop[0]) - 1] = 1
                else:
                    new_pop[i][len(pop[0]) - 1] = 0
        return np.array(new_pop)