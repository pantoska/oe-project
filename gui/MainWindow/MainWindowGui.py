import wx

from gui.Settings.Settings import SettingsControl, VAL_ELITY_STRATEGY_PERCENT, VAL_ELITY_STRATEGY_AMOUNT

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class MainFrame(wx.Frame):
    def __init__(self, parent, title, minsize=(850, 500)):
        super().__init__(parent=parent, title=title)
        self.SetMinSize(minsize)
        self.panel = MainPanel(self)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        # window
        self.settingswindow = SettingsControl(self)
        # self.Bind(wx.EVT_BUTTON, self.updateVarsBox)
        self.vars_box_sizer = None
        self.plotBox = None
        self.timeText = None
        self.saveFilePathText = None

        self.drawContent()

    def drawContent(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self._initDrawPlot(), 2, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(self.drawSetVarsBoxTitle(), 0, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(self.drawSetVarsBox(), 0, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(self.drawOutputFilePath(), 0, wx.ALL | wx.EXPAND, 10)

        main_sizer.Add(self.drawFooter(), 0, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(main_sizer)

    def drawFooter(self):
        sizer = wx.BoxSizer()
        sizer.Add(self.drawTime(), 1)
        sizer.AddStretchSpacer()
        sizer.Add(self.drawSettingsButton(), 0, wx.ALIGN_RIGHT)
        return sizer

    def drawTime(self):
        self.timeText = wx.StaticText(self)
        self.timeText.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.updateTime(-1)
        return self.timeText

    def updateTime(self, secounds):
        txt = "Czas kalkulacji:"
        if (secounds > 0):
            txt = txt + " " + str(secounds) + "s"

        self.timeText.SetLabelMarkup("<b>" + txt + "</b>")

    def drawSettingsButton(self):
        button = wx.Button(parent=self, label="Ustawienia")
        button.Bind(wx.EVT_BUTTON, self.onClickSettingsButton)
        return button

    def onClickSettingsButton(self, event):
        self.settingswindow.showWindow()

    def _initDrawPlot(self):
        self.plotBox = wx.BoxSizer()
        box = wx.StaticBox(self)
        # box.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.plotBox.Add(box, 1, wx.EXPAND, 0)
        return self.plotBox

    def drawPlot(self, figureArray):
        for indx in reversed(range(len(self.plotBox.GetChildren()))):
            self.plotBox.GetItem(indx).DeleteWindows()
            self.plotBox.Remove(indx)

        for fig in figureArray:
            plot = FigureCanvas(self, -1, fig)
            plot.SetMinSize((200, 200))
            self.plotBox.Add(plot, 1, wx.SHAPED, 0)

        self.Layout()

    def drawSetVarsBoxTitle(self):
        boxTitle = wx.StaticText(self, wx.ID_ANY, "Ustawione wartości", style=wx.ALIGN_CENTER)
        boxTitle.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        return boxTitle

    def drawSetVarsBox(self):
        self.vars_box_sizer = wx.BoxSizer()
        self.vars_box_sizer.Add(self.drawSetVarLeft(), 1)
        self.vars_box_sizer.Add(self.drawSetVarMiddle(), 1)
        self.vars_box_sizer.Add(self.drawSetVarRight(), 1)
        return self.vars_box_sizer

    def updateVarsBox(self):
        for indx in reversed(range(len(self.vars_box_sizer.GetChildren()))):
            self.vars_box_sizer.GetItem(indx).DeleteWindows()
            self.vars_box_sizer.Remove(indx)

        self.vars_box_sizer.Add(self.drawSetVarLeft(), 1)
        self.vars_box_sizer.Add(self.drawSetVarMiddle(), 1)
        self.vars_box_sizer.Add(self.drawSetVarRight(), 1)
        self.saveFilePathText.SetLabel(self.settingswindow.getSaveFilePath())
        self.Layout()

    def drawSetVarLeft(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        function_type = wx.StaticText(self, wx.ID_ANY, self.settingswindow.getTypeOfFunctionName())

        x_division = wx.StaticText(self, wx.ID_ANY, 'Przedział X funkcji: (' +
                                   str(self.settingswindow.getXdivisionStart()) + ', ' +
                                   str(self.settingswindow.getXdivisionEnd()) + ')')

        y_division = wx.StaticText(self, wx.ID_ANY, 'Przedział Y funkcji: (' +
                                   str(self.settingswindow.getYdivisionStart()) + ', ' +
                                   str(self.settingswindow.getYdivisionEnd()) + ')')

        Z_division = wx.StaticText(self, wx.ID_ANY, 'Przedział Z funkcji: (' +
                                   str(self.settingswindow.getZdivisionStart()) + ', ' +
                                   str(self.settingswindow.getZdivisionEnd()) + ')')

        sizer.Add(function_type, 0)
        sizer.Add(x_division, 0)
        sizer.Add(y_division, 0)
        sizer.Add(Z_division, 0)
        return sizer

    def drawSetVarMiddle(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        chromosome_precision = wx.StaticText(self, wx.ID_ANY, 'Dokładność chromosomu: ' +
                                             str(self.settingswindow.getChromosomePrecision()))
        population = wx.StaticText(self, wx.ID_ANY, 'Wielkość populacji: ' +
                                   str(self.settingswindow.getPopulation()))
        epoch = wx.StaticText(self, wx.ID_ANY, 'Wielkość populacji: ' +
                              str(self.settingswindow.getEpoch()))
        type_selection = wx.StaticText(self, wx.ID_ANY, 'Metoda selekcji: ' +
                                       self.settingswindow.getTypeSelectionName())
        division_selection = wx.StaticText(self, wx.ID_ANY, 'Wielkość populacji: ' +
                                           str(self.settingswindow.getDivisionSelection()))
        type_outbread = wx.StaticText(self, wx.ID_ANY, 'Krzyżowanie: ' +
                                      self.settingswindow.getTypeOutBreadName())
        propability_outbread = wx.StaticText(self, wx.ID_ANY, 'Prawdopodobieństwo krzyżowania: ' +
                                             str(self.settingswindow.getPropabilityOutBread()))

        sizer.Add(chromosome_precision, 0)
        sizer.Add(population, 0)
        sizer.Add(epoch, 0)
        sizer.Add(type_selection, 0)
        sizer.Add(division_selection, 0)
        sizer.Add(type_outbread, 0)
        sizer.Add(propability_outbread, 0)

        return sizer

    def drawSetVarRight(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        type_margin_mutation = wx.StaticText(self, wx.ID_ANY, 'Mutacja: ' +
                                             str(self.settingswindow.getTypeMutationName()))
        propability_margin_mutation = wx.StaticText(self, wx.ID_ANY, 'Prawdopodobieństwo mutacji brzegowej: ' +
                                                    str(self.settingswindow.getPropabilityMutation()))
        propability_inversion = wx.StaticText(self, wx.ID_ANY, 'Prawdopodobieństwo inwersji: ' +
                                              str(self.settingswindow.getPropabilityInversion()), )

        elity_text = 'Liczba osobników przechodzaca do kolejnej populacji: '
        if self.settingswindow.getElityStartegy() == VAL_ELITY_STRATEGY_PERCENT:
            elity_text = elity_text + str(self.settingswindow.getElityPercent()) + '%'
        elif self.settingswindow.getElityStartegy() == VAL_ELITY_STRATEGY_AMOUNT:
            elity_text = elity_text + str(self.settingswindow.getElityPercent()) + ' osobników'

        elity = wx.StaticText(self, wx.ID_ANY, elity_text)

        sizer.Add(type_margin_mutation, 0)
        sizer.Add(propability_margin_mutation, 0)
        sizer.Add(propability_inversion, 0)
        sizer.Add(elity, 0)

        return sizer

    def drawOutputFilePath(self):
        self.saveFilePathText = wx.StaticText(self, wx.ID_ANY)

        return self.saveFilePathText
