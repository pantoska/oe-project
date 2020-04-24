import numpy as np

class Statistics:

    def generate_stats(self, evaluated_pop, generations):

        values =[]
        std_devs = []
        min_values =[]
        max_values = []
        avg_values =[]
        gen = []

        for index, el in enumerate(evaluated_pop):
            gen.append(index)
            values.append(np.around(el))
            std_devs.append(np.around(np.std(el)))
            min_values.append(np.around(np.min(el)))
            max_values.append(np.around(np.max(el)))
            avg_values.append(np.around(np.around(el)))

        return values, std_devs, min_values, max_values, avg_values, gen