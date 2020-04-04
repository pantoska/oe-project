import wx
import wx.lib.scrolledpanel

from gui.Settings.SettingsConst import *


class SettingsFrame(wx.Frame):
    def __init__(self, parent, title, values={}, minsize=(600, 500)):
        super().__init__(parent=parent, title=title, style=wx.CAPTION | wx.RESIZE_BORDER)

        self.panel = None
        self.values = values

        self.SetMinSize(minsize)
        self.SetMaxSize((700, 800))
        self.SetSize(minsize)
        self.OnInit()

    def OnInit(self):
        self.panel = SettingsPanel(self, self.values)
        self.panel.Show()


class SettingsPanel(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, values={}):
        super().__init__(parent=parent, style=wx.VSCROLL)

        self.values = values
        self.radio_function_type_ch1 = None
        self.radio_function_type_ch2 = None
        self.input_x_division_start = None
        self.input_x_division_end = None
        self.input_y_division_start = None
        self.input_y_division_end = None
        self.input_z_division_start = None
        self.input_z_division_end = None
        self.button_ok = None
        self.button_cancel = None
        self.input_chromosome_precision = None
        self.input_population = None
        self.input_epoch = None
        self.input_type_selection = None
        self.input_division_selection = None
        self.input_type_outbread = None
        self.input_propability_outbread = None
        self.input_type_margin_mutation = None
        self.input_propability_mutation = None
        self.input_propability_inversion = None
        self.radio_elity_startegy_ch1 = None
        self.radio_elity_startegy_ch2 = None
        self.input_elity_strategy_percent = None
        self.input_elity_strategy_amount = None
        self.input_file_path = None

        self.drawContent()

    def drawContent(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.AddSpacer(15)
        main_sizer.Add(self.drawSectionTitle(SETTINGS_INSIDE_TITLE, 13), 0, wx.CENTER, 15)
        main_sizer.Add(self.drawChoiceTypeFunction(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawXdivision(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawYdivision(), 0, wx.ALL | wx.EXPAND, 5)
        # main_sizer.Add(self.drawZdivision(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawSectionTitle(SETTINGS_INSIDE_TITLE2, 11), 0, wx.CENTER, 15)
        main_sizer.Add(self.drawPrecision(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawPopulationInput(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawEpochInput(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawSelectionChoice(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawSelectionChoiceDivisions(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawOutbreadChoice(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawOutbreadPropability(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawMarginMutationChoice(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawMarginMutationPropability(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawInversionPropability(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawElityStrategyLabel(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawElityStrategyRadio(), 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.drawDirPicker(), 0, wx.ALL | wx.EXPAND, 5)

        main_sizer.AddStretchSpacer()
        main_sizer.Add(self.drawButtons(), 0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 15)
        main_sizer.AddSpacer(10)

        self.ShowScrollbars(wx.SHOW_SB_NEVER, wx.SHOW_SB_DEFAULT)
        self.SetupScrolling()
        self.SetSizer(main_sizer)
        main_sizer.Fit(self)
        self.Layout()
        self.Fit()

        # Refresh number inputs
        self.onClickEnityStartegyCh()

    def drawSectionTitle(self, label, font_size=10):
        titleinsidebox = wx.StaticText(self, wx.ID_ANY, label)
        titleinsidebox.SetFont(wx.Font(font_size, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        return titleinsidebox

    def drawButtons(self):
        self.button_ok = wx.Button(self, wx.ID_OK, 'OK')
        self.button_cancel = wx.Button(self, wx.ID_CANCEL)
        self.button_cancel.Bind(wx.EVT_BUTTON, self.onCancel)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.button_ok, 0, wx.ALL, 5)
        sizer.Add(self.button_cancel, 0, wx.ALL, 5)
        sizer.AddSpacer(10)
        return sizer

    def onCancel(self, event):
        self.GetParent().Close()

    def drawChoiceTypeFunction(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.radio_function_type_ch1 = wx.RadioButton(self, label='Minimalizacja funkcji', name='selectFunctionType')
        self.radio_function_type_ch2 = wx.RadioButton(self, label='Maksymalizacja funkcji', name='selectFunctionType')

        if 'function_type_ch1' in self.values:
            self.radio_function_type_ch1.SetValue(self.values['function_type_ch1'])

        if 'function_type_ch2' in self.values:
            self.radio_function_type_ch2.SetValue(self.values['function_type_ch2'])

        sizer.Add(self.radio_function_type_ch1, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.radio_function_type_ch2, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawXdivision(self):
        sizer = wx.BoxSizer()
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Przedział X1 funkcji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)

        self.input_x_division_start = wx.SpinCtrlDouble(self, wx.ID_ANY, min=-100000000, max=100000000)
        self.input_x_division_end = wx.SpinCtrlDouble(self, wx.ID_ANY, min=-100000000, max=100000000)
        if 'x_division_start' in self.values:
            self.input_x_division_start.SetValue(self.values['x_division_start'])

        if 'x_division_end' in self.values:
            self.input_x_division_end.SetValue(self.values['x_division_end'])

        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_x_division_start, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.input_x_division_end, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawYdivision(self):
        sizer = wx.BoxSizer()
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Przedział X2 funkcji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)

        self.input_y_division_start = wx.SpinCtrlDouble(self, wx.ID_ANY, min=-100000000, max=100000000)
        self.input_y_division_end = wx.SpinCtrlDouble(self, wx.ID_ANY, min=-100000000, max=100000000)
        if 'y_division_start' in self.values:
            self.input_y_division_start.SetValue(self.values['y_division_start'])

        if 'y_division_end' in self.values:
            self.input_y_division_end.SetValue(self.values['y_division_end'])

        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_y_division_start, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.input_y_division_end, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawZdivision(self):
        sizer = wx.BoxSizer()
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Przedział z funkcji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)

        self.input_z_division_start = wx.SpinCtrlDouble(self, wx.ID_ANY, min=-100000000, max=100000000)
        self.input_z_division_end = wx.SpinCtrlDouble(self, wx.ID_ANY, min=-100000000, max=100000000)
        if 'z_division_start' in self.values:
            self.input_z_division_start.SetValue(self.values['z_division_start'])

        if 'z_division_end' in self.values:
            self.input_z_division_end.SetValue(self.values['z_division_end'])

        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_z_division_start, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.input_z_division_end, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawPrecision(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Dokladność chromosomu:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_chromosome_precision = wx.SpinCtrlDouble(self, wx.ID_ANY, min=0, max=0.01)
        if 'chromosome_precision' in self.values:
            self.input_chromosome_precision.SetValue(self.values['chromosome_precision'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_chromosome_precision, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawPopulationInput(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Wielkość populacji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_population = wx.SpinCtrl(self, wx.ID_ANY, min=100, max=99999999)
        if 'population' in self.values:
            self.input_population.SetValue(self.values['population'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_population, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawEpochInput(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Liczba epok:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_epoch = wx.SpinCtrl(self, wx.ID_ANY, min=2, max=1000)
        if 'epoch' in self.values:
            self.input_epoch.SetValue(self.values['epoch'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_epoch, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawSelectionChoice(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Metoda selekcji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_type_selection = wx.Choice(self, choices=["", "", ""])
        self.input_type_selection.SetString(VAL_SELECTIONCHOICE_WHEEL, VAL_SELECTIONCHOICE_WHEEL_STR)
        self.input_type_selection.SetString(VAL_SELECTIONCHOICE_TURNAMENT_SELECTION,
                                            VAL_SELECTIONCHOICE_TURNAMENT_SELECTION_STR)
        self.input_type_selection.SetString(VAL_SELECTIONCHOICE_THEBEST, VAL_SELECTIONCHOICE_THEBEST_STR)

        if 'type_selection' in self.values:
            self.input_type_selection.SetSelection(self.values['type_selection'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_type_selection, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawSelectionChoiceDivisions(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Na ile przedziałów zostanie podzielona:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_division_selection = wx.SpinCtrl(self, wx.ID_ANY, min=2, max=1000)
        if 'division_selection' in self.values:
            self.input_division_selection.SetValue(self.values['division_selection'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_division_selection, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawOutbreadChoice(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Krzyżowanie:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_type_outbread = wx.Choice(self, choices=["", "", "", ""])
        self.input_type_outbread.SetString(VAL_OUTBREAD_ONE_POINT, VAL_OUTBREAD_ONE_POINT_STR)
        self.input_type_outbread.SetString(VAL_OUTBREAD_TWO_POINT, VAL_OUTBREAD_TWO_POINT_STR)
        self.input_type_outbread.SetString(VAL_OUTBREAD_TRIPLE_POINT, VAL_OUTBREAD_TRIPLE_POINT_STR)
        self.input_type_outbread.SetString(VAL_OUTBREAD_HOMOGENEOUS, VAL_OUTBREAD_HOMOGENEOUS_STR)

        if 'type_outbread' in self.values:
            self.input_type_outbread.SetSelection(self.values['type_outbread'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_type_outbread, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawOutbreadPropability(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Prawdopodobieństwo krzyżowania:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_propability_outbread = wx.SpinCtrlDouble(self, wx.ID_ANY, min=0, max=1, inc=0.01)
        if 'propability_outbread' in self.values:
            self.input_propability_outbread.SetValue(self.values['propability_outbread'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_propability_outbread, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawMarginMutationChoice(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Mutacja:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_type_margin_mutation = wx.Choice(self, choices=["", "", ""])
        self.input_type_margin_mutation.SetString(VAl_MUTATION_ONE_POINT, VAl_MUTATION_ONE_POINT_STR)
        self.input_type_margin_mutation.SetString(VAl_MUTATION_TWO_POINT, VAl_MUTATION_TWO_POINT_STR)
        self.input_type_margin_mutation.SetString(VAL_MUTATION_MARGIN, VAL_MUTATION_MARGIN_STR)

        if 'type_mutation' in self.values:
            self.input_type_margin_mutation.SetSelection(self.values['type_mutation'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_type_margin_mutation, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawMarginMutationPropability(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Prawdopodobieństwo mutacji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_propability_mutation = wx.SpinCtrlDouble(self, wx.ID_ANY, min=0, max=1, inc=0.01)
        if 'propability_mutation' in self.values:
            self.input_propability_mutation.SetValue(self.values['propability_mutation'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_propability_mutation, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawInversionPropability(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Prawdopodobieństwo inwersji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)
        self.input_propability_inversion = wx.SpinCtrlDouble(self, wx.ID_ANY, min=0, max=1, inc=0.01)
        if 'PropabilityInversion' in self.values:
            self.input_propability_inversion.SetValue(self.values['PropabilityInversion'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_propability_inversion, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawElityStrategyLabel(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Liczba osobników przechodzących do kolejnej populacji:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.EXPAND)

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def drawElityStrategyRadio(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.radio_elity_startegy_ch1 = wx.RadioButton(self,
                                                       label='Procent osobników:',
                                                       name='selectInutStartegy',
                                                       size=(SETTINGS_LABEL_MIN_WIDTH - 10, SETTINGS_LABEL_HEIGHT),
                                                       style=wx.RB_GROUP)
        self.radio_elity_startegy_ch2 = wx.RadioButton(self,
                                                       label='Liczba osobników:',
                                                       name='selectInutStartegy',
                                                       size=(SETTINGS_LABEL_MIN_WIDTH - 10, SETTINGS_LABEL_HEIGHT))

        if 'radio_elity_startegy_ch1' in self.values:
            self.radio_elity_startegy_ch1.SetValue(self.values['radio_elity_startegy_ch1'])

        if 'radio_elity_startegy_ch2' in self.values:
            self.radio_elity_startegy_ch2.SetValue(self.values['radio_elity_startegy_ch2'])

        self.radio_elity_startegy_ch1.Bind(wx.EVT_RADIOBUTTON, self.onClickEnityStartegyCh)
        self.radio_elity_startegy_ch2.Bind(wx.EVT_RADIOBUTTON, self.onClickEnityStartegyCh)

        sizerCh1 = wx.BoxSizer()
        sizerCh1.Add(self.radio_elity_startegy_ch1, 0, wx.ALL, 5)
        sizerCh1.Add(self.drawElityStrategyPercent(), 1, wx.ALL | wx.EXPAND, 5)

        sizerCh2 = wx.BoxSizer()
        sizerCh2.Add(self.radio_elity_startegy_ch2, 0, wx.ALL, 5)
        sizerCh2.Add(self.drawElityStrategyAmount(), 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(sizerCh1, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(sizerCh2, 1, wx.ALL | wx.EXPAND, 5)
        return sizer

    def onClickEnityStartegyCh(self, event=None):
        if self.radio_elity_startegy_ch1.GetValue():
            self.input_elity_strategy_percent.Enable()
        else:
            self.input_elity_strategy_percent.Disable()

        if self.radio_elity_startegy_ch2.GetValue():
            self.input_elity_strategy_amount.Enable()
        else:
            self.input_elity_strategy_amount.Disable()

        self.Refresh()

    def drawElityStrategyPercent(self):
        self.input_elity_strategy_percent = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=100)
        self.input_elity_strategy_percent.Disable()

        if 'elity_strategy_percent' in self.values:
            self.input_elity_strategy_percent.SetValue(self.values['elity_strategy_percent'])

        return self.input_elity_strategy_percent

    def drawElityStrategyAmount(self):
        self.input_elity_strategy_amount = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=10000000)
        self.input_elity_strategy_amount.Disable()

        if 'elity_strategy_amount' in self.values:
            self.input_elity_strategy_amount.SetValue(self.values['elity_strategy_amount'])

        return self.input_elity_strategy_amount

    def drawDirPicker(self):
        inputlabel = wx.StaticText(self, wx.ID_ANY, "Miejsce zapisy pliku wynikowego:",
                                   size=(SETTINGS_LABEL_MIN_WIDTH, SETTINGS_LABEL_HEIGHT),
                                   style=wx.ST_NO_AUTORESIZE)

        self.input_file_path = wx.FilePickerCtrl(self, wildcard="Coma Separated Values: *.csv",
                                                 style=wx.FLP_SAVE | wx.FLP_USE_TEXTCTRL | wx.FLP_OVERWRITE_PROMPT
                                                 | wx.FLP_SMALL)
        if 'save_file_path' in self.values:
            self.input_file_path.SetPath(self.values['save_file_path'])

        sizer = wx.BoxSizer()
        sizer.Add(inputlabel, 0, wx.ALL, 5)
        sizer.Add(self.input_file_path, 1, wx.ALL | wx.EXPAND, 5)
        return sizer
