import numpy as np
import wx
from matplotlib import cm

from Algorithm.Inversion.InversionAlgorithm import InversionAlgorithm
from Algorithm.Selection.Best import Best
from Algorithm.Selection.Roulette import Roulette
from Algorithm.Selection.Tournament import Tournament
from Algorithm.Cross.CrossAlgorithms import CrossAlgorithms
from Algorithm.Mutation.MutationAlgorithm import MutationAlgorithm
from Algorithm.MainAlgorithm.MainAlgorithm import MainAlgorithm
import matplotlib.pyplot as plt
import math

from gui.MainWindow.MainWindowGui import MainFrame

class AppMain(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # handle event from child
        self.Bind(wx.EVT_BUTTON, self.SetData)
        self.frame = MainFrame(None, "Funkcja jakaś tam!")
        # init Frame
        self.InitFrame()

    def InitFrame(self):
        self.frame.Show()

    def SetData(self, event):

        #===================================CONSTRUCTORS==========
        main = MainAlgorithm()
        inver = InversionAlgorithm()
        best = Best()
        roulette = Roulette()
        tournament = Tournament()
        cross = CrossAlgorithms()
        mutate = MutationAlgorithm()
        #==========================================================

        #jaki przedzial poczatkowy
        range_start = -10
        #jaki przedzial koncowy
        range_stop = 10
        #procent najlepszych
        percent = 20
        #ilosc generacji
        generations = 200
        #prawdopodobienstwo skrzyzowania
        pk = 0.01
        #prawdopodobienstwo mutacji
        pm = 0.03

        B, dx = main.get_amount_bits(range_start,range_stop, self.frame.panel.settingswindow.getChromosomePrecision())
        N = 2

        pop = main.generate_population(self.frame.panel.settingswindow.getPopulation(), N, B)
        evaluated_pop = main.evaluate_population(main.func, pop, N, B, range_start, self.frame.panel.settingswindow.getChromosomePrecision())

        best_pop, best_value = best.get_best_max(pop, evaluated_pop, percent)

        roulette_pop, roulette_value = roulette.roulette_max(pop, evaluated_pop, 40)
        tour_max, tour_value = tournament.tournament_max(pop, evaluated_pop, 3)

        remain, remain_value = inver.elite_strategy(best_pop, np.array(best_value), 0, percent)

        # lista srednich
        list_mean = np.empty(0)
        list_mean = np.append(list_mean, (sum(evaluated_pop) / self.frame.panel.settingswindow.getPopulation()))

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

        best_p = np.array(best_pop)
        length = len(pop) - len(best_p)

        #===============================================================================

        for g in range(generations):
            pop = roulette.roulette_max(pop, evaluated_pop, 40)
            pop = cross.single_cross(pop, pk, length)

            # new_pop_cross = cross.single_cross(best_p, 0.7, length)
            # new_pop_cross2 = cross.double_cross(best_p, 0.7, length)
            # new_pop_cross3 = cross.triple_cross(best_p, 0.7, length)
            # another_cross = cross.homogeneous_cross(best_p, 0.7, length)

            pop = mutate.mutate_one_points(pop, pm)

            # edge = mutate.mutate_edge(new_pop_cross,0.7)
            #
            # one_point = mutate.mutate_one_points(new_pop_cross2, 0.7)
            #
            # two_point = mutate.mutate_two_points(new_pop_cross2, 0.7)

            pop = inver.inversion(pop, pk)

            evaluated_pop = main.evaluate_population(main.func, pop, N, B, -2, dx)

            list_mean = np.append(list_mean, (sum(evaluated_pop) / len(evaluated_pop)))
            list_values = np.append(list_values, evaluated_pop)

            sumary = 0
            for i in list_values[-length_list_values:]:
                sumary += (i - list_mean[-1]) ** 2

            result = math.sqrt(sumary / length_list_values)
            list_sd = np.append(list_sd, result)

        print("liczba iteracji", g)
        print("srednia",list_mean,"wartosci", list_values,"odchylenie", list_sd)

        self.refreshSetData()
        self.drawPlot()

    def refreshSetData(self):
        self.frame.panel.updateVarsBox()

    def drawPlot(self):
        X = np.arange(-15, 15, 0.55)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)

        figure = plt.figure()
        axes = figure.gca(projection='3d')
        axes.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

        self.frame.panel.drawPlot(figure)
        self.frame.panel.updateTime(10)


