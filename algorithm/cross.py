import numpy as np
import random


class Cross:

    def cross(self, pop, pop_size,  probability, cross_times):

        new_individual = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        new_pop = []

        for i in range(0, int(pop_size / 2)):
            rnd = np.random.random()
            first_index = np.random.randint(0, len(pop)-1)
            second_index = np.random.randint(0, len(pop)-1)
            if (rnd < probability):
                if cross_times == 1:
                    pivot = random.sample(range(0, len(pop[0]) - 1), 1)
                    new_individual[first_index] = np.concatenate((pop[first_index][:pivot[0]], pop[second_index][pivot[0]:]))
                    new_individual[second_index] = np.concatenate((pop[second_index][:pivot[0]], temp[first_index][pivot[0]:]))
                if cross_times == 2:

                    sorted_pivots = np.sort(random.sample(range(0, len(pop) - 1), 2))

                    new_individual[first_index] = np.concatenate((pop[first_index][:sorted_pivots[0]],pop[second_index][sorted_pivots[0]:sorted_pivots[1]],pop[first_index][sorted_pivots[1]:]))
                    new_individual[second_index] = np.concatenate((pop[second_index][:sorted_pivots[0]],pop[i][sorted_pivots[0]:sorted_pivots[1]], temp[second_index][sorted_pivots[1]:]))

                if cross_times == 3:

                    sorted_pivots = np.sort(random.sample(range(0, len(pop) - 1), 3))

                    new_individual[first_index] = np.concatenate((pop[first_index][:sorted_pivots[0]],pop[second_index][sorted_pivots[0]:sorted_pivots[1]],pop[first_index][sorted_pivots[1]:sorted_pivots[2]],pop[second_index][sorted_pivots[2]:]))
                    new_individual[second_index] = np.concatenate((pop[second_index][:sorted_pivots[0]], temp[first_index][sorted_pivots[0]:sorted_pivots[1]],pop[second_index][sorted_pivots[1]:sorted_pivots[2]],temp[first_index][sorted_pivots[2]:]))

            new_pop.append(new_individual[first_index])
            new_pop.append(new_individual[second_index])

        if (len(new_pop) < pop_size):
            for i in range(0, pop_size - len(new_pop)):
                new_pop.append(pop[np.random.randint(0, len(pop) - 1)])

        return np.array(new_pop)

    def uniform_cross(self, pop, pop_size, probability):

        new_individual = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        new_pop = []

        for i in range(0, (len(pop) // 2)):

            rnd = np.random.random()
            first_index = np.random.randint(0, len(pop) - 1)
            second_index = np.random.randint(0, len(pop) - 1)

            if (rnd < probability):
                for j in range(len(pop[0]) - 1):
                    new_individual[first_index][j] = new_individual[second_index][j]
                    new_individual[second_index][j] = temp[first_index][j]

                new_pop.append(new_individual[first_index])
                new_pop.append(new_individual[second_index])

        if (len(new_pop) < pop_size):
            for i in range(0,pop_size - len(new_pop)):
                new_pop.append(pop[np.random.randint(0, len(pop) - 1)])

        return new_pop

    def heuristic_cross(self, pop, probability):
        new_pop = []
        copy_pop = np.array(pop, copy=True)

        while 0 < len(copy_pop):
            if len(copy_pop) == 1:
                new_pop.append(np.array(copy_pop[0]))
                break

            cross_index = np.random.randint(len(copy_pop))
            while 0 == cross_index:
                cross_index = np.random.randint(len(copy_pop))

            k = np.random.random()

            if probability > np.random.random():
                if copy_pop[cross_index][0] > copy_pop[0][0]:
                    new_x1 = k * (copy_pop[cross_index][0] - copy_pop[0][0]) + copy_pop[0][0]
                    new_y1 = k * (copy_pop[cross_index][1] - copy_pop[0][1]) + copy_pop[0][1]

                new_pop.append(np.array([new_x1, new_y1]))
            else:
                new_pop.append(np.array(copy_pop[0]))
                new_pop.append(np.array(copy_pop[cross_index]))

            copy_pop = np.delete(copy_pop, cross_index, 0)
            copy_pop = np.delete(copy_pop, 0, 0)

        return new_pop

    def arithmetic_cross(self, pop, probability):
        new_pop = []
        copy_pop = np.array(pop, copy=True)

        while len(new_pop) < len(pop):
            if len(copy_pop) == 1:
                new_pop.append(np.array(copy_pop[0]))
                break

            cross_index = np.random.randint(len(copy_pop))
            while 0 == cross_index:
                cross_index = np.random.randint(len(copy_pop))

            k = np.random.random()

            if probability > np.random.random():
                new_x1 = k * copy_pop[0][0] + (1 - k) * copy_pop[cross_index][0]
                new_x2 = k * copy_pop[cross_index][0] + (1 - k) * copy_pop[0][0]
                new_y1 = k * copy_pop[0][1] + (1 - k) * copy_pop[cross_index][1]
                new_y2 = k * copy_pop[cross_index][1] + (1 - k) * copy_pop[0][1]

                new_pop.append(np.array([new_x1, new_y1]))
                new_pop.append(np.array([new_x2, new_y2]))
            else:
                new_pop.append(np.array(copy_pop[0]))
                new_pop.append(np.array(copy_pop[cross_index]))

            copy_pop = np.delete(copy_pop, cross_index, 0)
            copy_pop = np.delete(copy_pop, 0, 0)

        return new_pop