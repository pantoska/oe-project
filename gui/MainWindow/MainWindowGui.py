import wx

from gui.Settings.Settings import SettingsControl, VAL_ELITY_STRATEGY_PERCENT, VAL_ELITY_STRATEGY_AMOUNT


class MainFrame(wx.Frame):
    def __init__(self, parent, title, minsize=(600, 500)):
        super().__init__(parent=parent, title=title)
        self.SetMinSize(minsize)
        self.OnInit()

    def OnInit(self):
        panel = MainPanel(self)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        # window
        self.settingswindow = SettingsControl(self.GetParent())

        self.drawContent()

    def drawContent(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.drawPlot(), 2, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(self.drawSetVarsBoxTitle(), 0, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(self.drawSetVarsBox(), 0, wx.ALL | wx.EXPAND, 10)

        main_sizer.Add(self.drawSettingsButton(), 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        main_sizer.SetSizeHints(self)
        self.SetSizer(main_sizer)

    def drawSettingsButton(self):
        button = wx.Button(parent=self, label="Ustawienia")
        button.Bind(wx.EVT_BUTTON, self.onClickSettingsButton)
        return button

    def onClickSettingsButton(self, event):
        self.settingswindow.showWindow()

    def drawPlot(self):
        return wx.StaticBox(self)

    def drawSetVarsBoxTitle(self):
        boxTitle = wx.StaticText(self, wx.ID_ANY, "Ustawione wartości", style=wx.ALIGN_CENTER)

        return boxTitle

    def drawSetVarsBox(self):
        sizer = wx.BoxSizer()
        sizer.Add(self.drawSetVarLeft(), 1)
        sizer.Add(self.drawSetVarRight(), 1)
        return sizer

    def drawSetVarLeft(self):
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

        type_margin_mutation = wx.StaticText(self, wx.ID_ANY, 'Mutacja brzegowa: ' +
                                             str(self.settingswindow.getTypeMarginMutationName()))
        propability_margin_mutation = wx.StaticText(self, wx.ID_ANY, 'Prawdopodobieństwo mutacji brzegowej: ' +
                                   str(self.settingswindow.getPropabilityMarginMutation()))
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
