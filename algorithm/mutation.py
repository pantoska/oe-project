import numpy as np

class Mutation:

    def mutate(self, pop, pm, points):
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

    def mutate_edge(self, pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(len(pop)):
            random = np.random.random()
            if random < pm:
                if pop[i][len(pop[0]) - 1] == 0:
                    new_pop[i][len(pop[0]) - 1] = 1
                else:
                    new_pop[i][len(pop[0]) - 1] = 0
        return np.array(new_pop)

    def mutate_change_index(self, pop, probability):
        new_pop = np.array(pop, copy=True)
        for i in range(len(new_pop)):
            if probability > np.random.random():
                new_pop[i] = np.array([new_pop[i][1], new_pop[i][0]])

        return new_pop

    def mutate_even(self, pop, probability, min_x1, max_x1, min_x2, max_x2):
        new_pop = np.array(pop, copy=True)
        half_probability = probability / 2
        for i in range(len(new_pop)):
            random = np.random.random()
            if probability > random:
                if half_probability > random:
                    new_pop[i] = np.array([np.random.uniform(min_x1, max_x1), new_pop[i][1]])
                else:
                    new_pop[i] = np.array([new_pop[i][0], np.random.uniform(min_x2, max_x2)])

        return new_pop
