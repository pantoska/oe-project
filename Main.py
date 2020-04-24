from gui.App import AppMain
from Algorithm.MainAlgorithm.MainAlgorithm import MainAlgorithm
from Algorithm.main_algorithm import Algorithm

if __name__ == "__main__":
    app = AppMain()
    app.MainLoop()
    # best_value, time,values, std_devs, min_values, max_values, avg_values, gen = Algorithm.run(Algorithm(), -10, 10, -10, 10,
    #                                  100, 10, 0.01, True, False, 40,
    #                                  False, False, True, 2, 0.8, 3, False,
    #                                  0.6, False, 1, 0.8)
    # print(best_value, time)