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

from Algorithm.main_algorithm import Algorithm

from gui.MainWindow.MainWindowGui import MainFrame
from gui.Settings.SettingsConst import VAL_SELECTIONCHOICE_WHEEL, VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR, \
    VAL_SELECTIONCHOICE_THEBEST_STR, VAL_OUTBREAD_ONE_POINT_STR, VAL_OUTBREAD_TWO_POINT_STR, \
    VAL_OUTBREAD_TRIPLE_POINT_STR, VAl_MUTATION_ONE_POINT_STR, VAl_MUTATION_TWO_POINT_STR, VAL_MUTATION_MARGIN_STR, \
    VAL_MINIMALIZATION, VAL_MAXIMALIZATION


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

        import time

        # ===================================CONSTRUCTORS==========
        main = MainAlgorithm()
        inver = InversionAlgorithm()
        best = Best()
        roulette = Roulette()
        tournament = Tournament()
        cross = CrossAlgorithms()
        mutate = MutationAlgorithm()
        # ==========================================================
        max = False
        min = False
        cross_point = 1
        uniform_cross = False
        edge_mutation = False
        mutation_point = 1

        # funkcja optymalizacji
        if(self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION):
            max = True
        else:
            min = False

        # precyzja chromosomu
        chromosome_prec = self.frame.panel.settingswindow.getChromosomePrecision()

        # jaki przedzial poczatkowy x1
        range_start_x1 = self.frame.panel.settingswindow.getXdivisionStart()
        # jaki przedzial koncowy
        range_stop_x1 = self.frame.panel.settingswindow.getXdivisionEnd()

        # jaki przedzial poczatkowy x2
        range_start_x2 = self.frame.panel.settingswindow.getYdivisionStart()
        # jaki przedzial koncowy
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

        if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_THEBEST_STR:
            best = True
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
            tournament = True
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_WHEEL:
            roulette = True

        # prawdopodobienstwo skrzyzowania
        pk = self.frame.panel.settingswindow.getPropabilityOutBread()

        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_ONE_POINT_STR:
            cross_point = 1
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TWO_POINT_STR:
            cross_point = 2
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TRIPLE_POINT_STR:
            cross_point = 3

        #UNIFORM
        if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TRIPLE_POINT_STR:
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

        # best_value, time = Algorithm.run(range_start_x1, range_stop_x1, range_start_x2, range_stop_x2,
        #                                  generations, population_size, chromosome_prec, max, min, percent,
        #                                  best, roulette, tournament, tour_size, pk,cross_point, uniform_cross,
        #                                  pm, edge_mutation, mutation_point, inv)
        # best_value, time = Algorithm.run(-10, 10, -10, 10,
        #                                  100, 6, 0.01, True, False, 40,
        #                                  True, False , False, 5, 0.8, 1, False,
        #                                  0.6, False, 1, 0.8)
        # print(best_value, time)


        # zapis pliku
        # path = self.frame.panel.settingswindow.getSaveFilePath()

        # start_all_program =  time.time()
        #
        # B, dx = main.get_amount_bits(range_start, range_stop, chromosome_prec)
        # N = 2
        #
        # pop = main.generate_population(population_size, N, B)
        # evaluated_pop = main.evaluate_population(main.func, pop, N, B, range_start, chromosome_prec)
        #
        # best_pop = []
        # best_value = []
        #
        # if(self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION):
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_THEBEST_STR:
        #         best_pop, best_value = best.get_best_max(pop, evaluated_pop, percent)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
        #         best_pop, best_value = tournament.tournament_max(pop, evaluated_pop, tour)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_WHEEL:
        #         best_pop = roulette.roulette_max(pop, evaluated_pop, percent)
        # else:
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_THEBEST_STR:
        #         best_pop, best_value = best.get_best_min(pop, evaluated_pop, percent)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
        #         best_pop, best_value = tournament.tournament_min(pop, evaluated_pop, tour)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_WHEEL:
        #         best_pop = roulette.roulette_min(pop, evaluated_pop, percent)
        #
        #
        # remain, remain_value = inver.elite_strategy(best_pop, np.array(best_value), 0, percent)
        #
        # # lista srednich
        # list_mean = np.empty(0)
        # list_mean = np.append(list_mean, (sum(evaluated_pop) / population_size))
        #
        # # lista wartosci
        # list_values = np.empty(0)
        # list_values = np.append(list_values, evaluated_pop)
        #
        # # lista odchylenie standardowe
        # list_sd = np.empty(0)
        # length_list_values = len(list_values)
        #
        # sumary = 0
        # for i in range(len(list_values)):
        #     sumary += (list_values[i] - list_mean) ** 2
        #
        # result = math.sqrt(sumary / len(list_values))
        # list_sd = np.append(list_sd, result)
        #
        # if(self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION):
        #
        #     for i in range(0, len(remain), 1):
        #         pop = np.delete(pop, np.argmax(evaluated_pop), 0)
        #         evaluated_pop = np.delete(evaluated_pop, np.argmax(evaluated_pop), 0)
        #
        # if(self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION):
        #
        #     for i in range(0, len(remain), 1):
        #         pop = np.delete(pop, np.argmin(evaluated_pop), 0)
        #         evaluated_pop = np.delete(evaluated_pop, np.argmin(evaluated_pop), 0)
        #
        # best_p = np.array(best_pop)
        # length = len(pop) - len(best_p)
        #
        # # ===============================================================================
        #
        # for g in range(generations):
        #
        #     if (self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION):
        #
        #         if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_THEBEST_STR:
        #             pop, best_value = best.get_best_max(pop, evaluated_pop, percent)
        #
        #         if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
        #             pop, best_value = tournament.tournament_max(pop, evaluated_pop, tour)
        #
        #         if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_WHEEL:
        #             pop = roulette.roulette_max(pop, evaluated_pop, percent)
        #
        #     else:
        #
        #         if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_THEBEST_STR:
        #             pop, best_value = best.get_best_min(pop, evaluated_pop, percent)
        #
        #         if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR:
        #             pop, best_value = tournament.tournament_min(pop, evaluated_pop, tour)
        #
        #         if self.frame.panel.settingswindow.getTypeSelection() == VAL_SELECTIONCHOICE_WHEEL:
        #             pop = roulette.roulette_min(pop, evaluated_pop, percent)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_ONE_POINT_STR:
        #         pop = cross.single_cross(pop, pk, length)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TWO_POINT_STR:
        #         pop = cross.double_cross(pop, pk, length)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TRIPLE_POINT_STR:
        #         pop = cross.triple_cross(pop, pk, length)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_OUTBREAD_TRIPLE_POINT_STR:
        #         pop = cross.homogeneous_cross(pop, pk, length)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAl_MUTATION_ONE_POINT_STR:
        #         pop = mutate.mutate_one_points(pop, pm)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAl_MUTATION_TWO_POINT_STR:
        #         pop = mutate.mutate_two_points(pop, pm)
        #
        #     if self.frame.panel.settingswindow.getTypeSelection() == VAL_MUTATION_MARGIN_STR:
        #         pop = mutate.mutate_edge(pop, pm)
        #
        #     pop = inver.inversion(pop, inv)
        #
        #     evaluated_pop = main.evaluate_population(main.func, pop, N, B, range_start, dx)
        #
        #     list_mean = np.append(list_mean, (sum(evaluated_pop) / len(evaluated_pop)))
        #     list_values = np.append(list_values, evaluated_pop)
        #
        #     if (self.frame.panel.settingswindow.getTypeOfFunction() == VAL_MAXIMALIZATION):
        #         self.frame.panel.setMinimumValue(max(list_mean), range_start, range_stop)
        #     else:
        #         self.frame.panel.setMinimumValue(min(list_mean), range_start, range_stop)
        #
        #     sumary = 0
        #     for i in list_values[-length_list_values:]:
        #         sumary += (i - list_mean[-1]) ** 2
        #
        #     result = math.sqrt(sumary / length_list_values)
        #     list_sd = np.append(list_sd, result)
        #
        # stop_all_program =  time.time()
        # time = abs(stop_all_program - start_all_program)
        # self.frame.panel.updateTime(time)
        # print(time)
        #
        # list_values = np.reshape(list_values, (generations+1,len(evaluated_pop)))
        #
        # gen = []
        # for i in range(generations + 1):
        #     gen.append(i)

        best_value, time, values, std_devs, min_values, max_values, avg_values, gen = Algorithm.run(Algorithm(), -10,
                                                                                                    10, -10, 10,
                                                                                                    100, 10, 0.01, True,
                                                                                                    False, 40,
                                                                                                    False, False, True,
                                                                                                    2, 0.8, 3, False,
                                                                                                    0.6, False, 1, 0.8)
        print(best_value, time)


        self.refreshSetData()
        self.drawPlot(avg_values, values, std_devs, gen)
        self.saveToFileArrays(avg_values,values,std_devs)

    def refreshSetData(self):
        self.frame.panel.updateVarsBox()

    def drawPlot(self, list_mean, list_values, list_sd, generation):
        X = generation

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(X, list_mean)
        ax.set_title("Średnie wartości funkcji")

        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax1.plot(X, list_sd)
        ax1.set_title("Odchylenie standardowe")

        best = []
        for i in list_values:
            best.append(max(i))

        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot(X, np.array(best))
        ax2.set_title("Wartości funkcji")

        self.frame.panel.drawPlot([fig, fig1, fig2])
        print(self.frame.panel.settingswindow.getSaveFilePathlist_mean())

    def saveToFileArrays(self, list_mean, list_values, list_sd):
        np.savetxt(self.frame.panel.settingswindow.getSaveFilePathlist_mean(), list_mean, delimiter=',')
        np.savetxt(self.frame.panel.settingswindow.getSaveFilePathlist_values(), list_values, delimiter=',')
        np.savetxt(self.frame.panel.settingswindow.getSaveFilePathlist_sd(), list_sd, delimiter=',')
