import numpy as np
import wx

import matplotlib.pyplot as plt

from algorithm.main_algorithm import Algorithm

from gui.MainWindow.MainWindowGui import MainFrame
from gui.Settings.SettingsConst import VAL_SELECTIONCHOICE_WHEEL, VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR, \
    VAL_SELECTIONCHOICE_THEBEST_STR, VAL_OUTBREAD_ONE_POINT_STR, VAL_OUTBREAD_TWO_POINT_STR, \
    VAL_OUTBREAD_TRIPLE_POINT_STR, VAl_MUTATION_ONE_POINT_STR, VAl_MUTATION_TWO_POINT_STR, VAL_MUTATION_MARGIN_STR, \
    VAL_MINIMALIZATION, VAL_MAXIMALIZATION, VAL_OUTBREAD_HOMOGENEOUS, VAL_SELECTIONCHOICE_WHEEL_STR


class AppMain(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # handle event from child
        self.Bind(wx.EVT_BUTTON, self.SetData)
        self.frame = MainFrame(None, "Klasyczny algorytm genetyczny")
        # init Frame
        self.InitFrame()

    def InitFrame(self):
        self.frame.Show()

    def SetData(self, event):

        max_func = False
        min_func = False
        cross_point = 1
        uniform_cross = False
        edge_mutation = False
        mutation_point = 1
        best_selection = False
        roulette_selection = False
        tournament_selection = False

        # funkcja optymalizacji
        if (self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION):
            max_func = True
        if (self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MINIMALIZATION):
            min_func = True

        # precyzja chromosomu
        chromosome_prec = self.frame.panel.settingswindow.getChromosomePrecision()

        # jaki przedzial poczatkowy x1
        range_start_x1 = self.frame.panel.settingswindow.getXdivisionStart()
        # jaki przedzial koncowy x1
        range_stop_x1 = self.frame.panel.settingswindow.getXdivisionEnd()

        # jaki przedzial poczatkowy x2
        range_start_x2 = self.frame.panel.settingswindow.getYdivisionStart()
        # jaki przedzial koncowy x2
        range_stop_x2 = self.frame.panel.settingswindow.getYdivisionEnd()

        # populacja
        population_size = self.frame.panel.settingswindow.getPopulation()
        # ilosc generacji
        generations = self.frame.panel.settingswindow.getEpoch()

        # procent najlepszych (do selekcji najlepszych)
        percent = self.frame.panel.settingswindow.getElityPercent()
        # ilosc turniei (do selekcji turniejowej)
        tour_size = self.frame.panel.settingswindow.getDivisionSelection()

        # ilosc najlepszych
        amount = self.frame.panel.settingswindow.getElityAmount()

        if self.frame.panel.settingswindow.getTypeSelectionName() == VAL_SELECTIONCHOICE_THEBEST_STR:
            best_selection = True
        elif self.frame.panel.settingswindow.getTypeSelectionName() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
            tournament_selection = True
        elif self.frame.panel.settingswindow.getTypeSelectionName() == VAL_SELECTIONCHOICE_WHEEL_STR:
            roulette_selection = True

        # prawdopodobienstwo skrzyzowania
        pk = self.frame.panel.settingswindow.getPropabilityOutBread()

        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_ONE_POINT_STR:
            cross_point = 1
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TWO_POINT_STR:
            cross_point = 2
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TRIPLE_POINT_STR:
            cross_point = 3

        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_HOMOGENEOUS:
            uniform_cross = True

        # prawdopodobienstwo mutacji
        pm = self.frame.panel.settingswindow.getPropabilityMutation()

        if self.frame.panel.settingswindow.getTypeSelection() == VAl_MUTATION_ONE_POINT_STR:
            mutation_point = 1
        if self.frame.panel.settingswindow.getTypeSelection() == VAl_MUTATION_TWO_POINT_STR:
            mutation_point = 2
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_MUTATION_MARGIN_STR:
            edge_mutation = True

        # inwersja
        inv = self.frame.panel.settingswindow.getPropabilityInversion()

        # zapis pliku
        path = self.frame.panel.settingswindow.getSaveFilePath()

        best_value, time, values, std_devs, min_values, max_values, avg_values, gen, index_min, index_max = Algorithm.run(Algorithm(),
                                                                                                    range_start_x1,
                                                                                                    range_stop_x1,
                                                                                                    range_start_x2,
                                                                                                    range_stop_x2,
                                                                                                    generations,
                                                                                                    population_size,
                                                                                                    chromosome_prec,
                                                                                                    max_func, min_func,
                                                                                                    percent,
                                                                                                    best_selection, roulette_selection,
                                                                                                    tournament_selection,
                                                                                                    tour_size, pk,
                                                                                                    cross_point,
                                                                                                    uniform_cross,
                                                                                                    pm, edge_mutation,
                                                                                                    mutation_point, inv)

        # print(range_start_x1,
        #       range_stop_x1, range_start_x2, range_stop_x2,
        #       generations, population_size, chromosome_prec,
        #       max_func, min_func, percent,
        #       best, roulette, tournament,
        #       tour_size, pk, cross_point, uniform_cross,
        #       pm, edge_mutation, mutation_point, inv)

        self.frame.panel.updateTime(time)

        if self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION:
            self.frame.panel.setMaximumValue(max(max_values), min(range_start_x1,range_start_x2), max(range_stop_x1,range_stop_x2), index_max)
        elif self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MINIMALIZATION:
            self.frame.panel.setMinimumValue(min(min_values), min(range_start_x1,range_start_x2), max(range_stop_x1,range_stop_x2), index_min)

        self.refreshSetData()
        if max_func:
            self.drawPlot(avg_values, max_values, std_devs, gen, "Maksymalne wartości funkcji")
        if min_func:
            self.drawPlot(avg_values, min_values, std_devs, gen, "Minimalne wartości funkcji")

        self.saveToFileArrays(avg_values, values, std_devs)

    def refreshSetData(self):
        self.frame.panel.updateVarsBox()

    def drawPlot(self, list_mean, list_values, list_sd, generation, title):
        X = generation

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(X, list_mean)
        ax.set_title("Średnie wartości funkcji")

        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax1.plot(X, list_sd)
        ax1.set_title("Odchylenie standardowe")

        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot(X, np.array(list_values))
        ax2.set_title(title)

        self.frame.panel.drawPlot([fig, fig1, fig2])
        print(self.frame.panel.settingswindow.getSaveFilePathlist_mean())

    def saveToFileArrays(self, list_mean, list_values, list_sd):
        np.savetxt(self.frame.panel.settingswindow.getSaveFilePathlist_mean(), list_mean, delimiter=',')
        np.savetxt(self.frame.panel.settingswindow.getSaveFilePathlist_values(), list_values, delimiter=',')
        np.savetxt(self.frame.panel.settingswindow.getSaveFilePathlist_sd(), list_sd, delimiter=',')

