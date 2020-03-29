import matplotlib.pyplot as plt
import numpy as np

from algorithm import *

# Na wykresach funkcji 3D przedstaw położenie osobników z pierwszej populacji,
# w połowie ewolucji oraz końcowej populacji. Zaznacz wyraźnie położenie najlepszeg rozwiązania.
#
# Na wykresach 2D przedstaw przebieg wartości z list z zebranymi statystykami
# (listy list_best, list_best_generation, list_mean) w zależności od numeru pokolenia.
def draw(pop, pop_size, B, dx):
    fig = plt.figure()
    l = np.empty(0)
    for i in range(pop_size):
        l = np.append(l, decode_individual(pop[i], 2, B, -2, dx))
    l, k = l.reshape(2, pop_size)

    ax = fig.add_subplot(111, projection='3d')

    j = fun([l, k])
    tt = np.argmax(j)
    ax.scatter(l[tt], k[tt], j[tt], zdir='z', s=20, c='blue', depthshade=True)
    l = np.delete(l, tt)
    k = np.delete(k, tt)
    j = np.delete(j, tt)
    ax.scatter(l, k, j, zdir='z', s=20, c='red', depthshade=True)
    ax.set_title('Wykres')
    ax.set_xlabel('X')
    ax.set_xlim(-15, 5)
    ax.set_ylabel('Y')
    ax.set_ylim(-3, 3)
    ax.set_zlabel('Z')
    ax.set_zlim(0, 200)
    plt.show()


def function(fun, pop_size, pk, pm, generations, dx):
    B, dx = nbits(-2, 2, dx)
    N = 2
    pop = gen_population(pop_size, N, B)
    evaluated_pop = evaluate_population(fun, pop, N, B, -2, dx)
    _, best_value = get_best(pop, evaluated_pop)
    best_sol = best_value
    best_generation = 0
    list_mean = np.empty(0)
    list_mean = np.append(list_mean, (sum(evaluated_pop) / pop_size))
    list_best = np.empty(0)
    list_best = np.append(list_best, best_sol)
    list_best_generation = np.empty(0)
    list_best_generation = np.append(list_best_generation, best_sol)
    print('pierwsza populacja:')
    draw(pop, pop_size, B, dx)
    for g in range(generations):
        if g == pop_size // 2:
            print('srodkowa populacja:')
            draw(pop, pop_size, B, dx)
        pop = roulette(pop, evaluated_pop)
        pop = cross(pop, pk)
        pop = mutate(pop, pm)

        evaluated_pop = evaluate_population(fun, pop, N, B, -2, dx)
        _, best_value = get_best(pop, evaluated_pop)
        if best_value > best_sol:
            best_sol = best_value
            best_generation = g + 1
        list_mean = np.append(list_mean, (sum(evaluated_pop) / pop_size))
        list_best = np.append(list_best, best_sol)
        list_best_generation = np.append(list_best_generation, best_value)

    print('ostatnia populacja:')
    draw(pop, pop_size, B, dx)
    draw(pop, pop_size, B, dx)
    return best_sol, best_generation, list_best, list_best_generation, list_mean


np.random.seed()
best_sol, best_generation, list_best, list_best_generation, list_mean = function(fun, 60, 0.7, 0.01, 200, 1e-10)

ax = plt.subplot(111)
plt.plot(list_mean, label="sredni osobnik")
plt.plot(list_best_generation, label="najlepszy osobnik w danej populacji")
plt.plot(list_best, label="najlepszy osobnik")
leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.show()