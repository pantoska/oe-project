import numpy as np

class Algorithm:

    #funkcja bodajże 3
    def fun(x):
        return 100 * np.sqrt(np.fabs(x[1] - 0.01 * (x[0] ** 2))) + 0.01 * np.fabs(x[0] + 10)

    #najpierw minimalizacja
    #ilosc bitow potrzebnych do zakodowania liczby
    #należy podać zakres i krok, zwraca dokladniejszy krok
    def nbits(a, b, step):
        range = b - a
        #dlugosc binarnie
        amount_of_bits = int(range / step).bit_length()
        #nowy krok na podstawie dlugosci/
        new_step = range / (2**amount_of_bits - 1)
        return amount_of_bits, new_step

    #binary wektor, narazie [0,1,1,1,0]
    # P - liczba osobników, N liczba zmiennych, B liczba bitów na każdą ze zmiennych
    def gen_population(self, P, N, B):
        population = np.random.randint(2, size =(P,N*B))

    #rozkodowywanie osobników
    def decode_individual(individual, N, B, a, dx):
        temp = individual.reshape((N, B))
        decode_individual = np.ndarray(N)
        vector = []
        for i in range(0, B):
            vector.insert(0, 2 ** i)

        for j in range(0, N):
            decode_individual[j] = sum(np.multiply(vector, temp[j])) * dx + a
        return decode_individual

    #ocena osobników w populacji, funkcja celu
    def evaluate_population(func, pop, N, B, a, dx):
        # YOUR CODE HERE
        evaluated_pop = np.ndarray(int(pop.size / (B * N)))
        for i in range(int(pop.size / (B * N))):
            evaluated_pop[i] = func(func.decode_individual(pop[i], N, B, a, dx))
        return evaluated_pop

    #zwrocenie najlepszego osobnika
    def get_best(pop, evaluated_pop):
        best_value = max(evaluated_pop)
        best_individual = pop[np.argmax(evaluated_pop)]
        return best_individual, best_value

    # ruletka
    def roulette(pop, evaluated_pop):
        if np.ndarray.min(evaluated_pop) <= 0:
            evaluated_pop = evaluated_pop + abs(np.ndarray.min(evaluated_pop)) + 1
        d = np.cumsum(evaluated_pop)
        d = np.insert(d, 0, 0)

        new_pop = []
        i = 1
        counter = 0
        rand = np.random.random_sample()
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

        # raise NotImplementedError()
        return new_pop

    def cross(pop, pk):
        new_pop = np.array(pop, copy=True)
        temp = np.array(pop, copy=True)
        for i in range(0, len(pop), 2):
            if i + 1 >= len(pop):
                break
            rnd = np.random.random()
            if (rnd < pk):
                pivot = np.random.randint(1, pop.shape[1])
                # print(pivot)
                new_pop[i] = np.concatenate((pop[i][:pivot], pop[i + 1][pivot:]))
                new_pop[i + 1] = np.concatenate((pop[i + 1][:pivot], temp[i][pivot:]))
        return new_pop

    def mutate(pop, pm):
        new_pop = np.array(pop, copy=True)
        for i in range(pop.shape[0]):
            for j in range(pop.shape[1]):
                random = np.random.random()
                if random < pm:
                    if pop[i][j] == 0:
                        new_pop[i][j] = 1
                    else:
                        new_pop[i][j] = 0
        return new_pop

    # a,b,c,d,e = function(fun, 60, 0.7, 0.01, 200, 1e-10)
    def function(fun, pop_size, pk, pm, generations, dx):

        #przedział od -2 do 2 z krokiem 1e-10, zwraca B - liczba bitów, dx  - nową dokładność
        B, dx = fun.nbits(-2, 2, dx)
        #liczba zmiennych
        N = 2
        # pop size - liczba osobników, liczba zmiennych, liczba bitów na każdą z zmiennych zwraca populacje zakodowanych osobnikow
        pop = fun.gen_population(pop_size, N, B)

        #funkcja celu na każdym z osobników, populacja osobników, liczba zmiennych, liczba bitów, początek predziału, krok dokładnosci
        evaluated_pop = fun.evaluate_population(fun, pop, N, B, -2, dx)

        #zwracanie najlepszego osobnika
        _, best_value = fun.get_best(pop, evaluated_pop)


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
            _, best_value = fun.get_best(pop, evaluated_pop)
            if best_value > best_sol:
                best_sol = best_value
                best_generation = g + 1
            list_mean = np.append(list_mean, (sum(evaluated_pop) / pop_size))
            list_best = np.append(list_best, best_sol)
            list_best_generation = np.append(list_best_generation, best_value)

        return best_sol, best_generation, list_best, list_best_generation, list_mean