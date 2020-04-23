import numpy as np
import timeit
import math


from Algorithm.Inversion.InversionAlgorithm import InversionAlgorithm
from Algorithm.Selection.Best import Best
from Algorithm.Selection.Roulette import Roulette
from Algorithm.Selection.Tournament import Tournament
from Algorithm.Cross.CrossAlgorithms import CrossAlgorithms
from Algorithm.Mutation.MutationAlgorithm import MutationAlgorithm


class MainAlgorithm:


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


