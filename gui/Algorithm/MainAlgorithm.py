import numpy as np


class MainAlgorithm:

    # x - array table with x1, x2, another function for testing
    def function(self, x):
        return 2 * x[0] ** 2 + 5
        # return 100 * np.sqrt(np.fabs(x[1] - 0.01 * (x[0] ** 2))) + 0.01 * np.fabs(x[0] + 10)

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
            evaluated_pop[i] = func(decode_individual(population[i], amount_variables, amount_of_bits, a, step))
        return evaluated_pop

    best = elite_strategy(pop, evaluated_pop, 0, 0.7)
    pop = np.delete(pop, np.argwhere(pop == best))

    # te mutacje i inne i na koncu

    pop = np.append(pop, best)

    # i do kolejnej generacji
