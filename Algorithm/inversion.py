import numpy as np

class Inversion:

    def inversion(pop, pk):
        new_pop = np.array(pop, copy=True)
        for i in range(0, len(pop)):
            rnd = np.random.random()
            if (rnd < pk):
                first_pivot = np.random.randint(1, len(pop[0]) - 1)
                second_pivot = np.random.randint(1, len(pop[0]) - 1)

                sorted_pivots = np.sort(np.array([first_pivot, second_pivot]))

                new_part = []
                for j in range(sorted_pivots[0], sorted_pivots[1]):
                    new_part.append(pop[i][j])
                new_part.reverse()

                new_pop[i] = pop[i][:sorted_pivots[0]] + new_part +  pop[i][sorted_pivots[1]:]

        return np.array(new_pop)