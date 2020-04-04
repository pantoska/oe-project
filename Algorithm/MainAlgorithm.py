import numpy as np
import timeit
import math

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from Algorithm.Inversion.InversionAlgorithm import InversionAlgorithm
from Algorithm.Selection.Best import Best
from Algorithm.Selection.Roulette import Roulette
from Algorithm.Selection.Tournament import Tournament
from Algorithm.Cross.CrossAlgorithms import CrossAlgorithms
from Algorithm.Mutation.MutationAlgorithm import MutationAlgorithm


class MainAlgorithm:

    # x - array table with x1, x2, another function for testing
    def func(self, x):
        # return 2 * x[0] ** 2 + 5
        return 100 * np.sqrt(np.fabs(x[1] - 0.01 * (x[0] ** 2))) + 0.01 * np.fabs(x[0] + 10)

    # get number of bits needed to encode number from range [a,b] with step
    def get_amount_bits(self, a, b, step):
        range = b - a
        amount_of_bits = int(range / step).bit_length()
        new_step = range / (2 ** amount_of_bits - 1)
        return amount_of_bits, new_step

    # generate population
    def generate_population(self, amount_individuals, amount_variables, amount_bits):
        population = np.random.randint(2, size=(amount_individuals, amount_variables * amount_bits))
        return population

    # decode individual from binary
    def decode_individual(self, individual_binary, amount_variables, amount_of_bits, a, step):
        temp = individual_binary.reshape((amount_variables, amount_of_bits))
        decode_ind = np.ndarray(amount_variables)
        vector = []
        for i in range(0, amount_of_bits):
            vector.insert(0, 2 ** i)

        for j in range(0, amount_variables):
            decode_ind[j] = sum(np.multiply(vector, temp[j])) * step + a
        return decode_ind

    # calculate function on every individual
    def evaluate_population(self, func, population, amount_variables, amount_of_bits, a, step):
        evaluated_pop = np.ndarray(int(population.size / (amount_of_bits * amount_variables)))
        for i in range(int(population.size / (amount_of_bits * amount_variables))):
            evaluated_pop[i] = func(self.decode_individual(population[i], amount_variables, amount_of_bits, a, step))
        return evaluated_pop

    def function(self, pop_size, pk, pm, generations, dx):

        inver = InversionAlgorithm()
        best = Best()
        roulette = Roulette()
        tournament = Tournament()
        cross = CrossAlgorithms()
        mutate = MutationAlgorithm()

        start_all_program = timeit.timeit()

        B, dx = self.get_amount_bits(-2, 2, 0.01)
        N = 2

        pop = self.generate_population(pop_size, N, B)
        evaluated_pop = self.evaluate_population(self.func, pop, N, B, -2, dx)

        best_pop, best_value = best.get_best_max(pop, evaluated_pop, 40)

        remain, remain_value = inver.elite_strategy(best_pop, np.array(best_value), 0, 20)

        # lista srednich
        list_mean = np.empty(0)
        list_mean = np.append(list_mean, (sum(evaluated_pop) / pop_size))

        # lista wartosci
        list_values = np.empty(0)
        list_values = np.append(list_values, evaluated_pop)

        # lista odchylenie standardowe
        list_sd = np.empty(0)
        length_list_values = len(list_values)

        sumary = 0
        for i in range(len(list_values)):
            sumary += (list_values[i] - list_mean) ** 2

        result = math.sqrt(sumary / len(list_values))
        list_sd = np.append(list_sd, result)

        for i in range(0, len(remain), 1):
            pop = np.delete(pop, np.argmax(evaluated_pop), 0)
            evaluated_pop = np.delete(evaluated_pop, np.argmax(evaluated_pop), 0)

        # new_pop = roulette.roulette_max(pop, evaluated_pop, 40)
        # tour_max, tour_value = tournament.tournament_max(pop, evaluated_pop, 3)

        best_p = np.array(best_pop)
        length = len(pop) - len(best_p)

        # liczba generacji
        for g in range(generations):
            pop = roulette.roulette_max(pop, evaluated_pop, 40)
            pop = cross.single_cross(pop, pk, length)
            pop = mutate.mutate_one_points(pop, pk)
            pop = inver.inversion(pop, pk)

            evaluated_pop = self.evaluate_population(self.func, pop, N, B, -2, dx)
            best_pop, best_value = best.get_best_max(pop, evaluated_pop, 40)

            list_mean = np.append(list_mean, (sum(evaluated_pop) / pop_size))
            list_values = np.append(list_values, evaluated_pop)

            sumary = 0
            for i in list_values[-length_list_values:]:
                sumary += (i - list_mean[-1]) ** 2

            result = math.sqrt(sumary / length_list_values)
            list_sd = np.append(list_sd, result)

        print("srednie", list_mean)
        print("wartosci", list_values)
        print("ostatnie", list_sd)

        stop_all_program = timeit.timeit()

        print(abs(stop_all_program - start_all_program))

        return list_mean
        # new_pop_cross = cross.single_cross(best_p, 0.7, length)
        # new_pop_cross2 = cross.double_cross(best_p, 0.7, length)
        # new_pop_cross3 = cross.triple_cross(best_p, 0.7, length)
        # another_cross = cross.homogeneous_cross(best_p, 0.7, length)

        # edge = mutate.mutate_edge(new_pop_cross,0.7)
        #
        # one_point = mutate.mutate_one_points(new_pop_cross2, 0.7)
        #
        # two_point = mutate.mutate_two_points(new_pop_cross2, 0.7)
        #
        # inver = inver.inversion(new_pop_cross, 0.7)
