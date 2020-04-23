import numpy as np
import random


class Cross:

    def cross(pop, pop_size,  probability, cross_times):

        new_individual = pop.copy()
        temp = np.array(pop, copy=True)
        new_pop = []

        for i in range(0, int(pop_size / 2)):
            rnd = np.random.random()
            first_index = np.random.randint(0, len(pop)-1)
            second_index = np.random.randint(0, len(pop)-1)
            if (rnd < probability):
                if cross_times == 1:
                    pivot = random.sample(range(0, pop[0] + 1), 1)
                    new_individual[first_index] = pop[first_index][:pivot] + pop[second_index][pivot:]
                    new_individual[second_index] = pop[second_index][:pivot] + temp[first_index][pivot:]
                if cross_times == 2:

                    sorted_pivots = np.sort(random.sample(range(0, pop[0] + 1), 2))

                    new_individual[first_index] = pop[first_index][:sorted_pivots[0]] + pop[second_index][sorted_pivots[0]:sorted_pivots[1]] + pop[first_index][sorted_pivots[1]:]
                    new_individual[second_index] = pop[second_index][:sorted_pivots[0]] + pop[i][sorted_pivots[0]:sorted_pivots[1]] + temp[second_index][sorted_pivots[1]:]

                if cross_times == 3:

                    sorted_pivots = np.sort(random.sample(range(0, pop[0] + 1), 3))

                    new_individual[first_index] = pop[first_index][:sorted_pivots[0]] + pop[second_index][sorted_pivots[0]:sorted_pivots[1]] +pop[first_index][sorted_pivots[1]:sorted_pivots[2]] +pop[second_index][sorted_pivots[2]:]
                    new_individual[second_index] = pop[second_index][:sorted_pivots[0]] + temp[first_index][sorted_pivots[0]:sorted_pivots[1]] +pop[second_index][sorted_pivots[1]:sorted_pivots[2]]+temp[first_index][sorted_pivots[2]:]

            new_pop.append(new_individual[first_index])
            new_pop.append(new_individual[second_index])

        if (len(np.array(new_pop)) < len(pop)):
            new_pop.append(pop[np.random.randint(0, len(pop[0]) - 1)])

        return np.array(new_pop)

    def uniform_cross(pop, probability):

        new_individual = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        new_pop = []

        for i in range(0, (len(pop)// 2) + 1, 2):

            first_index = np.random.randint(0, len(pop) - 1)
            second_index = np.random.randint(0, len(pop) - 1)
            rnd = np.random.random()

            if (rnd < probability):
                for j in range(len(pop[0]) - 1):
                    new_individual[first_index][j] = new_individual[second_index][j]
                    new_individual[second_index][j] = temp[first_index][j]

                new_pop.append(new_individual[first_index])
                new_pop.append(new_individual[second_index])

            if (len(np.array(new_pop)) < len(pop)):
                new_pop.append(pop[np.random.randint(0, len(pop[0]) - 1)])

        return new_pop