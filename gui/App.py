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
from gui.Settings.SettingsConst import VAL_SELECTIONCHOICE_WHEEL, VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR, \
    VAL_SELECTIONCHOICE_THEBEST_STR, VAL_OUTBREAD_ONE_POINT_STR, VAL_OUTBREAD_TWO_POINT_STR, \
    VAL_OUTBREAD_TRIPLE_POINT_STR, VAl_MUTATION_ONE_POINT_STR, VAl_MUTATION_TWO_POINT_STR, VAL_MUTATION_MARGIN_STR


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

        chromosome_prec = self.frame.panel.settingswindow.getChromosomePrecision()
        #jaki przedzial poczatkowy
        range_start = -10
        #jaki przedzial koncowy
        range_stop = 10
        #populacja
        population_size = self.frame.panel.settingswindow.getPopulation()
        #procent najlepszych
        percent = self.frame.panel.settingswindow.getElityPercent()
        #ilosc najlepszych
        amount = self.frame.panel.settingswindow.getElityPercent()
        #ilosc generacji
        generations = self.frame.panel.settingswindow.getEpoch()
        #prawdopodobienstwo skrzyzowania
        pk = self.frame.panel.settingswindow.getPropabilityOutBread()
        #prawdopodobienstwo mutacji
        pm = self.frame.panel.settingswindow.getPropabilityMutation()
        #ilosc turniei
        tour = self.frame.panel.settingswindow.getDivisionSelection()
        #inwersja
        inv = self.frame.panel.settingswindow.getPropabilityInversion()
        #zapis pliku
        path = self.frame.panel.settingswindow.getSaveFilePath()

        B, dx = main.get_amount_bits(range_start,range_stop, chromosome_prec)
        N = 2

        pop = main.generate_population(population_size, N, B)
        evaluated_pop = main.evaluate_population(main.func, pop, N, B, range_start, chromosome_prec)

        best_pop = []
        best_value = []
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_THEBEST_STR:
            best_pop, best_value = best.get_best_max(pop, evaluated_pop, percent)

        if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
            best_pop, best_value = tournament.tournament_max(pop, evaluated_pop, tour)

        if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_WHEEL:
            best_pop, best_value = roulette.roulette_max(pop, evaluated_pop, percent)

        remain, remain_value = inver.elite_strategy(best_pop, np.array(best_value), 0, percent)

        # lista srednich
        list_mean = np.empty(0)
        list_mean = np.append(list_mean, (sum(evaluated_pop) / population_size))

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

            if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_THEBEST_STR:
                pop, best_value = best.get_best_max(pop, evaluated_pop, percent)

            if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
                pop, best_value = tournament.tournament_max(pop, evaluated_pop, tour)

            if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_WHEEL:
                pop, best_value = roulette.roulette_max(pop, evaluated_pop, percent)


            if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_ONE_POINT_STR:
                pop = cross.single_cross(pop, pk, length)

            if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TWO_POINT_STR:
                pop = cross.double_cross(pop, pk, length)

            if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TRIPLE_POINT_STR:
                pop = cross.triple_cross(pop, pk, length)

            if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TRIPLE_POINT_STR:
                pop = cross.homogeneous_cross(pop, pk, length)

            if self.frame.panel.settingswindow.getTypeSelection() == VAl_MUTATION_ONE_POINT_STR:
                pop = mutate.mutate_one_points(pop, pm)

            if self.frame.panel.settingswindow.getTypeSelection() == VAl_MUTATION_TWO_POINT_STR:
                pop = mutate.mutate_two_points(pop, pm)

            if self.frame.panel.settingswindow.getTypeSelection() == VAL_MUTATION_MARGIN_STR:
                pop = mutate.mutate_edge(pop, pm)

            pop = inver.inversion(pop, inv)

            evaluated_pop = main.evaluate_population(main.func, pop, N, B, range_start, dx)

            list_mean = np.append(list_mean, (sum(evaluated_pop) / len(evaluated_pop)))
            list_values = np.append(list_values, evaluated_pop)

            sumary = 0
            for i in list_values[-length_list_values:]:
                sumary += (i - list_mean[-1]) ** 2

            result = math.sqrt(sumary / length_list_values)
            list_sd = np.append(list_sd, result)

        print("liczba iteracji", g+1)
        # print("srednia",list_mean,"wartosci", list_values,"odchylenie", list_sd)

        self.refreshSetData()
        self.drawPlot(list_mean, list_values, list_sd, g+1)

    def refreshSetData(self):
        self.frame.panel.updateVarsBox()

    def drawPlot(self, list_mean, list_values, list_sd, generation):
        X = np.arange(-15, 15, 0.55)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)

        figure = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter(l[tt], k[tt], j[tt], zdir='z', s=20, c='blue', depthshade=True)
        ax.set_title('Wykres')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z');


        self.frame.panel.drawPlot([figure, figure, figure])
        self.frame.panel.updateTime(10)


