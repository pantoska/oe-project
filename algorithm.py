import numpy as np


class Algorithm:

    # funkcja nr 6, funkcja dwóch zmiennych
    def fun(self, x):
        return 100 * np.sqrt(np.fabs(x[1] - 0.01 * (x[0] ** 2))) + 0.01 * np.fabs(x[0] + 10)

    # Implementacja binarnej reprezentacji chromosomu + konfiguracja dokładnośc
    # ilosc bitow potrzebnych do zakodowania liczby
    # należy podać zakres i krok, zwraca dokladniejszy krok
    def nbits(self, a, b, step):
        range = b - a
        # dlugosc binarnie
        amount_of_bits = int(range / step).bit_length()
        # nowy krok na podstawie dlugosci/
        new_step = range / (2 ** amount_of_bits - 1)
        return amount_of_bits, new_step

    # generuje populacje
    # P - rozmiar populacji, N liczba zmiennych, B liczba bitów na każdą ze zmiennych, czyli z funkcji wyżej
    def gen_population(self, P, N, B):
        population = np.random.randint(2, size=(P, N * B))
        return population

    # rozkodowywanie osobników z binarnej na dziesietna
    def decode_individual(self, individual, N, B, a, dx):
        temp = individual.reshape((N, B))
        decode_individual = np.ndarray(N)
        vector = []
        for i in range(0, B):
            vector.insert(0, 2 ** i)

        for j in range(0, N):
            decode_individual[j] = sum(np.multiply(vector, temp[j])) * dx + a
        return decode_individual

    # ocena osobników w populacji dla max, funkcja celu
    def evaluate_population_max(self, func, pop, N, B, a, dx):
        evaluated_pop = np.ndarray(int(pop.size / (B * N)))
        for i in range(int(pop.size / (B * N))):
            evaluated_pop[i] = func(func.decode_individual(pop[i], N, B, a, dx))
        return evaluated_pop

    # ocena osobników w populacji dla min, funkcja celu
    def evaluate_population_min(self, func, pop, N, B, a, dx):
        evaluated_pop = np.ndarray(int(pop.size / (B * N)))
        for i in range(int(pop.size / (B * N))):
            evaluated_pop[i] = 1 / (func(func.decode_individual(pop[i], N, B, a, dx)))
        return evaluated_pop

    def get_best_percent(self, pop, evaluated_pop, percent):
        copy_evaluated_pop = evaluated_pop[:]
        best_individual_percent = []
        best_value_percent = []

        for i in range(int(evaluated_pop.size * percent / 100)):
            print(copy_evaluated_pop)
            best_value = max(copy_evaluated_pop)
            # best_value = min(copy_evaluated_pop)
            best_value_percent.insert(i, best_value)
            best_individual_percent.insert(i, pop[np.argmax(copy_evaluated_pop)])
            copy_evaluated_pop = np.delete(copy_evaluated_pop, np.argmax(copy_evaluated_pop))
            i = i + 1

        return best_individual_percent, best_value_percent

    # tournament selection
    def tournament_selection(self, pop, evaluated_pop, tournament_size):
        copy_evaluated_pop = evaluated_pop[:]

        if (len(evaluated_pop) < tournament_size):
            return pop, evaluated_pop

        tour = []
        division = []
        i = 0

        while (i < tournament_size and len(copy_evaluated_pop) > tournament_size):
            select_index = np.random.randint(len(copy_evaluated_pop) - 1)
            division.append(copy_evaluated_pop[select_index])
            copy_evaluated_pop = np.delete(copy_evaluated_pop, select_index)
            i = i + 1
            if (i == tournament_size or len(copy_evaluated_pop) == tournament_size):
                tour.append(division)
                i = 0
                division = []

        if (len(copy_evaluated_pop) <= tournament_size):
            tour.append(copy_evaluated_pop)

        # selection the best from every tour
        new_pop = []
        new_ev_pop = []
        for el in tour:
            best_value_in_division = max(el)
            new_pop.append(pop[np.argmax(el)])
            new_ev_pop.append(best_value_in_division)

        return self.tournament_selection(new_pop, new_ev_pop, tournament_size)

    # ruletka
    def roulette(self, pop, evaluated_pop):
        # jesli mamy ujemne wartosci trzeba dac na wartosc bezwzgledna
        if np.ndarray.min(evaluated_pop) <= 0:
            evaluated_pop = evaluated_pop + abs(np.ndarray.min(evaluated_pop)) + 1
        # suma wszystkich i wstawienie na poczatek zera
        d = np.cumsum(evaluated_pop)
        d = np.insert(d, 0, 0)

        new_pop = []
        i = 1
        counter = 0
        rand = np.random.random_sample()
        # tyle razy aż do rozmiaru populacji
        while counter < evaluated_pop.size:
            if (d[i - 1] / d[d.size - 1]) <= rand < (d[i] / d[d.size - 1]):
                # print(rand)
                new_pop.append(pop[i - 1])
                # print([pop[i - 1]])
                counter = counter + 1
                i = 1
                rand = np.random.random_sample()
            else:
                i = i + 1
        new_pop = np.array(new_pop)

        return new_pop

    # krzyzowanie jednopunktowe, pk - prawdopodobienstwo skrzyzowania
    def single_cross(self, pop, pk):
        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        # shape[0] to ilosc rzedow, shape[1] to ilosc kolumn 2 to jest krok
        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            # prawdopodobienstwo z ktorym bedzie wylosowane
            rnd = np.random.random()
            if (rnd < pk):
                pivot = np.random.randint(1, pop.shape[1] - 1)
                print(pivot)
                new_pop[i] = np.concatenate((pop[i][:pivot], pop[i + 1][pivot:]))
                new_pop[i + 1] = np.concatenate((pop[i + 1][:pivot], temp[i][pivot:]))
        return new_pop

    # krzyzowanie dwupunktowe, pk - prawdopodobienstwo skrzyzowania
    def double_cross(self, pop, pk):
        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        # shape[0] to ilosc rzedow, shape[1] to ilosc kolumn 2 to jest krok
        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            rnd = np.random.random()
            if (rnd < pk):
                first_pivot = np.random.randint(1, pop.shape[1] - 1)
                second_pivot = np.random.randint(1, pop.shape[1] - 1)
                print(first_pivot, second_pivot)

                if (first_pivot == second_pivot):
                    while (first_pivot == second_pivot):
                        second_pivot = np.random.randint(1, pop.shape[1] - 1)

                first_part = []
                second_part = []
                max_pivot = max(first_pivot, second_pivot)
                min_pivot = min(first_pivot, second_pivot)
                for j in range(min_pivot, max_pivot, 1):
                    first_part.append(pop[i][j])
                    second_part.append(pop[i + 1][j])
                new_pop[i] = np.concatenate((pop[i][:min_pivot], second_part, pop[i][max_pivot:]))
                new_pop[i + 1] = np.concatenate((pop[i + 1][:min_pivot], first_part, temp[i][max_pivot:]))

        return new_pop

    def triple_cross(self, pop, pk):
        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            rnd = np.random.random()
            if (rnd < pk):
                first_pivot = np.random.randint(1, pop.shape[1] - 1)
                second_pivot = np.random.randint(1, pop.shape[1] - 1)
                third_pivot = np.random.randint(1, pop.shape[1] - 1)

                print(first_pivot, second_pivot, third_pivot)

                if (first_pivot == second_pivot or first_pivot == third_pivot or second_pivot == third_pivot):
                    while (first_pivot == second_pivot or first_pivot == third_pivot or second_pivot == third_pivot):
                        second_pivot = np.random.randint(1, pop.shape[1] - 1)
                        third_pivot = np.random.randint(1, pop.shape[1] - 1)

                first_part = []
                second_part = []
                third_part = []
                fourth_part = []

                pivots = [first_pivot, second_pivot, third_pivot]
                max_pivot = max(pivots)
                pivots.remove(max_pivot)
                medium_pivot = max(pivots)
                min_pivot = min(pivots)

                for j in range(min_pivot, medium_pivot, 1):
                    first_part.append(pop[i][j])
                    second_part.append(pop[i + 1][j])

                for k in range(medium_pivot, max_pivot, 1):
                    third_part.append(pop[i][k])
                    fourth_part.append(pop[i + 1][k])

                new_pop[i] = np.concatenate((pop[i][:min_pivot], second_part, third_part, pop[i][max_pivot:]))
                new_pop[i + 1] = np.concatenate((pop[i + 1][:min_pivot], first_part, fourth_part, temp[i][max_pivot:]))

        return new_pop

    def homogeneous_cross(self, pop, pk):
        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        for i in range(0, (pop.shape[0] // 2) + 1, 2):
            # prawdopodobienstwo z ktorym bedzie wylosowane
            rnd = np.random.random()
            if (rnd < pk):
                change = np.random.random()
                for j in range(pop.shape[1]):
                    # jesli wypadnie na 0
                    new_arr = []
                    new_arr2 = []
                    if (change < pk):
                        new_pop[i] = np.append(new_arr, pop[i][j])
                        new_pop[i + 1] = np.append(new_arr2, pop[i + 1][j])
                    # jesli wypadnie na 1
                    else:
                        new_pop[i] = np.append(new_arr, pop[i + 1][j])
                        new_pop[i + 1] = np.append(new_arr2, temp[i][j])

        return new_pop

    #mutacja jednopunktowa
    def mutate_one_points(self, pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(pop.shape[0]):
            random = np.random.random()
            random_index = np.random.randint(pop.shape[1])
            if random < pm:
                if pop[i][random_index] == 0:
                    new_pop[i][random_index] = 1
                else:
                    new_pop[i][random_index] = 0

        return new_pop

    # mutacja dwupunktowa
    def mutate_two_points(self, pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(pop.shape[0]):
            random = np.random.random()
            random_index_first = np.random.randint(pop.shape[1])
            random_index_second = np.random.randint(pop.shape[1])
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

    # mutacja brzegowa
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

    def inversion(self, pop, pk):

        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        # shape[0] to ilosc rzedow, shape[1] to ilosc kolumn 2 to jest krok
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

    # a,b,c,d,e = function(fun, 60, 0.7, 0.01, 200, 1e-10)
    # jesli liczba epok to liczba generacji
    def function(self, fun, pop_size, pk, pm, generations, dx):

        # przedział od -2 do 2 z krokiem 1e-10, zwraca B - liczba bitów, dx  - nową dokładność
        B, dx = fun.nbits(-2, 2, dx)
        # liczba zmiennych
        N = 2
        # pop size - liczba osobników, liczba zmiennych, liczba bitów na każdą z zmiennych zwraca populacje zakodowanych osobnikow
        pop = fun.gen_population(pop_size, N, B)

        # funkcja celu na każdym z osobników, populacja osobników, liczba zmiennych, liczba bitów, początek predziału, krok dokładnosci
        evaluated_pop = fun.evaluate_population(fun, pop, N, B, -2, dx)

        # zwracanie najlepszego osobnika
        _, best_value = fun.get_best_percent(pop, evaluated_pop)

        best_sol = best_value
        best_generation = 0
        list_mean = np.empty(0)
        list_mean = np.append(list_mean, (sum(evaluated_pop) / pop_size))
        list_best = np.empty(0)
        list_best = np.append(list_best, best_sol)
        list_best_generation = np.empty(0)
        list_best_generation = np.append(list_best_generation, best_sol)
        for g in range(generations):
            pop = fun.roulette(pop, evaluated_pop)
            pop = np.cross(pop, pk)
            pop = fun.mutate(pop, pm)

            evaluated_pop = fun.evaluate_population(fun, pop, N, B, -2, dx)
            _, best_value = fun.get_best_percent(pop, evaluated_pop)
            if best_value > best_sol:
                best_sol = best_value
                best_generation = g + 1
            list_mean = np.append(list_mean, (sum(evaluated_pop) / pop_size))
            list_best = np.append(list_best, best_sol)
            list_best_generation = np.append(list_best_generation, best_value)

        return best_sol, best_generation, list_best, list_best_generation, list_mean
