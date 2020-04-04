import wx
# from gui.App import AppMain
from Algorithm.MainAlgorithm import MainAlgorithm

if __name__ == "__main__":
    # app = AppMain()
    # app.MainLoop()

    main_algorithm = MainAlgorithm()
    main_algorithm.function(5, 0.7, 0.01, 20, 1e-10)
