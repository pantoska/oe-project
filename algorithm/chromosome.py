import numpy as np

class Chromosome:
    # get number of bits needed to encode number from range [a,b] with step
    def get_amount_bits(self, a, b, step):
        range = b - a
        amount_of_bits = int(range / step).bit_length()
        new_step = range / (2 ** amount_of_bits - 1)
        return amount_of_bits, new_step

    # decode individual from binary
    def decode_individual(self, individual_binary, x1_bits, x2_bits, x1_min, x2_min, x1_step, x2_step):
        x1_decoded = sum(individual_binary[0: x1_bits] * (2 ** np.arange(x1_bits)) * x1_step) + x1_min
        x2_decoded = sum(individual_binary[x1_bits:] * (2 ** np.arange(x2_bits)) * x2_step) + x2_min

        return np.array([x1_decoded, x2_decoded])