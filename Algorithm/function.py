import numpy as np

class Func:

    # x - array with x1, x2
    def func(self, x):
        # return 2 * x[0] ** 2 + 5
        return 100 * np.sqrt(np.fabs(x[1] - 0.01 * (x[0] ** 2))) + 0.01 * np.fabs(x[0] + 10)






