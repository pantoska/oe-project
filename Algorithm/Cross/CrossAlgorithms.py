import numpy as np


class CrossAlgorithms:

    def single_cross(self, pop, probability, times):

        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)

        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            rnd = np.random.random()
            if (rnd < probability):
                pivot = np.random.randint(1, pop.shape[1] - 1)
                new_pop[i] = np.concatenate((pop[i][:pivot], pop[i + 1][pivot:]))
                new_pop[i + 1] = np.concatenate((pop[i + 1][:pivot], temp[i][pivot:]))

        for i in range(0, times, 1):
            rnd1 = np.random.randint(0, pop.shape[0])
            rnd2 = np.random.randint(0, pop.shape[0])
            rnd = np.random.random()
            if (rnd < probability):
                pivot = np.random.randint(1, pop.shape[1] - 1)
                new_arr = np.array(np.concatenate((pop[rnd1][:pivot], pop[rnd2][pivot:])))
                new_pop = np.insert(new_pop, pop.shape[0], new_arr, 0)
            else:
                new_pop = np.insert(new_pop, pop.shape[0], new_pop[pop.shape[0] - 1], 0)

        return new_pop

    def double_cross(self, pop, probability, times):

        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)

        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            rnd = np.random.random()
            if (rnd < probability):
                first_pivot = np.random.randint(1, pop.shape[1] - 1)
                second_pivot = np.random.randint(1, pop.shape[1] - 1)

                if (first_pivot == second_pivot):
                    while (first_pivot == second_pivot):
                        second_pivot = np.random.randint(1, pop.shape[1] - 1)

                max_pivot = max(first_pivot, second_pivot)
                min_pivot = min(first_pivot, second_pivot)

                new_pop[i] = np.concatenate((pop[i][:min_pivot], pop[i + 1][min_pivot:max_pivot], pop[i][max_pivot:]))
                new_pop[i + 1] = np.concatenate(
                    (pop[i + 1][:min_pivot], pop[i][min_pivot:max_pivot], temp[i][max_pivot:]))

        for i in range(0, times, 1):
            rnd1 = np.random.randint(0, pop.shape[0])
            rnd2 = np.random.randint(0, pop.shape[0])
            rnd = np.random.random()
            if (rnd < probability):
                first_pivot = np.random.randint(1, pop.shape[1] - 1)
                second_pivot = np.random.randint(1, pop.shape[1] - 1)

                if (first_pivot == second_pivot):
                    while (first_pivot == second_pivot):
                        second_pivot = np.random.randint(1, pop.shape[1] - 1)

                max_pivot = max(first_pivot, second_pivot)
                min_pivot = min(first_pivot, second_pivot)

                new_arr = np.array(
                    np.concatenate((pop[rnd1][:min_pivot], pop[rnd2][min_pivot:max_pivot], pop[rnd1][max_pivot:])))
                new_pop = np.insert(new_pop, pop.shape[0], new_arr, 0)
            else:
                new_pop = np.insert(new_pop, pop.shape[0], new_pop[pop.shape[0] - 1], 0)

        return new_pop

    def triple_cross(self, pop, pk, times):

        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)

        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            rnd = np.random.random()
            if (rnd < pk):
                first_pivot = np.random.randint(1, pop.shape[1] - 1)
                second_pivot = np.random.randint(1, pop.shape[1] - 1)
                third_pivot = np.random.randint(1, pop.shape[1] - 1)

                if (first_pivot == second_pivot or first_pivot == third_pivot or second_pivot == third_pivot):
                    while (first_pivot == second_pivot or first_pivot == third_pivot or second_pivot == third_pivot):
                        second_pivot = np.random.randint(1, pop.shape[1] - 1)
                        third_pivot = np.random.randint(1, pop.shape[1] - 1)

                pivots = [first_pivot, second_pivot, third_pivot]
                max_pivot = max(pivots)
                pivots.remove(max_pivot)
                medium_pivot = max(pivots)
                min_pivot = min(pivots)

                new_pop[i] = np.concatenate((pop[i][:min_pivot], pop[i + 1][min_pivot:medium_pivot],
                                             pop[i][medium_pivot:max_pivot], pop[i + 1][max_pivot:]))
                new_pop[i + 1] = np.concatenate(
                    (pop[i + 1][:min_pivot], temp[i][min_pivot:medium_pivot], pop[i + 1][medium_pivot:max_pivot],
                     temp[i][max_pivot:]))

        for i in range(0, times, 1):

            rnd1 = np.random.randint(0, pop.shape[0])
            rnd2 = np.random.randint(0, pop.shape[0])

            rnd = np.random.random()
            if (rnd < pk):
                first_pivot = np.random.randint(1, pop.shape[1] - 1)
                second_pivot = np.random.randint(1, pop.shape[1] - 1)
                third_pivot = np.random.randint(1, pop.shape[1] - 1)

                if (first_pivot == second_pivot or first_pivot == third_pivot or second_pivot == third_pivot):
                    while (first_pivot == second_pivot or first_pivot == third_pivot or second_pivot == third_pivot):
                        second_pivot = np.random.randint(1, pop.shape[1] - 1)
                        third_pivot = np.random.randint(1, pop.shape[1] - 1)

                pivots = [first_pivot, second_pivot, third_pivot]
                max_pivot = max(pivots)
                pivots.remove(max_pivot)
                medium_pivot = max(pivots)
                min_pivot = min(pivots)

                new_arr = np.array(np.concatenate((pop[rnd1][:min_pivot], pop[rnd2][min_pivot:medium_pivot],
                                                   pop[rnd1][medium_pivot:max_pivot],
                                                   pop[rnd2][max_pivot:])))
                new_pop = np.insert(new_pop, pop.shape[0], new_arr, 0)
            else:
                new_pop = np.insert(new_pop, pop.shape[0], new_pop[np.random.randint(1, pop.shape[0])], 0)

        return new_pop

    def homogeneous_cross(self, pop, pk, times):

        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)

        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            rnd = np.random.random()
            if (rnd < pk):
                new_arr = []
                new_arr2 = []
                for j in range(pop.shape[1]):
                    change = np.random.random()
                    if (change < pk):
                        new_arr = np.append(new_arr, pop[i][j])
                        new_arr2 = np.append(new_arr2, pop[i + 1][j])
                    else:
                        new_arr = np.append(new_arr, pop[i + 1][j])
                        new_arr2 = np.append(new_arr2, temp[i][j])

                new_pop[i] = new_arr
                new_pop[i + 1] = new_arr2

        for i in range(0, times, 1):
            rnd1 = np.random.randint(0, pop.shape[0])
            rnd2 = np.random.randint(0, pop.shape[0])
            rnd = np.random.random()

            if (rnd < pk):
                new_arr = []
                for j in range(pop.shape[1]):
                    change = np.random.random()
                    if (change < pk):
                        new_arr = np.append(new_arr, pop[rnd1][j])
                    else:
                        new_arr = np.append(new_arr, pop[rnd2][j])

                new_pop = np.insert(new_pop, pop.shape[0], new_arr, 0)
            else:
                new_pop = np.insert(new_pop, pop.shape[0], new_pop[np.random.randint(1, pop.shape[0])], 0)

        return new_pop

    def arythmetic_cross(self, pop, probability):
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
