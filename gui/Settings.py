import wx

from gui.SettingsGui import SettingsFrame
from gui.SettingsConst import *


class SettingsControl:
    def __init__(self, parent):
        self.settingsWindow = None
        self.parent = parent
        self.values = {
            'chromosome_precision': 100,
            'population': 10,
            'epoch': 5,
            'type_selection': -1,
            'division_selection': 5,
            'type_outbread': -1,
            'propability_outbread': 0.1,
            'type_margin_mutation': -1,
            'propability_margin_mutation': 0.1,
            'PropabilityInversion': 0.1,
            'radio_elity_startegy_ch1': False,
            'radio_elity_startegy_ch2': False,
            'elity_strategy_percent': 0,
            'elity_strategy_amount': 0
        }

    def _updateValues(self):
        self.values = {
            'chromosome_precision': self.settingsWindow.panel.input_chromosome_precision.GetValue(),
            'population': self.settingsWindow.panel.input_population.GetValue(),
            'epoch': self.settingsWindow.panel.input_epoch.GetValue(),
            'type_selection': self.settingsWindow.panel.input_type_selection.GetSelection(),
            'division_selection': self.settingsWindow.panel.input_division_selection.GetValue(),
            'type_outbread': self.settingsWindow.panel.input_type_outbread.GetSelection(),
            'propability_outbread': self.settingsWindow.panel.input_propability_outbread.GetValue(),
            'type_margin_mutation': self.settingsWindow.panel.input_type_margin_mutation.GetSelection(),
            'propability_margin_mutation': self.settingsWindow.panel.input_propability_margin_mutation.GetValue(),
            'PropabilityInversion': self.settingsWindow.panel.input_propability_inversion.GetValue(),
            'radio_elity_startegy_ch1': self.settingsWindow.panel.radio_elity_startegy_ch1.GetValue(),
            'radio_elity_startegy_ch2': self.settingsWindow.panel.radio_elity_startegy_ch2.GetValue(),
            'elity_strategy_percent': self.settingsWindow.panel.input_elity_strategy_percent.GetValue(),
            'elity_strategy_amount': self.settingsWindow.panel.input_elity_strategy_amount.GetValue()
        }

    def showWindow(self):
        self.settingsWindow = SettingsFrame(self.parent, "Ustawienia", self.values )
        self.settingsWindow.panel.button_ok.Bind(wx.EVT_BUTTON, self.handleOkButton)
        self.settingsWindow.Show()

    def handleOkButton(self, event):
        self._updateValues()
        self.settingsWindow.Close()

    def getChromosomePrecision(self):
        return self.values['chromosome_precision']

    def getPopulation(self):
        return self.values['population']

    def getEpoch(self):
        return self.values['epoch']

    def getTypeSelection(self):
        return self.values['type_selection']

    def getDivisionSelection(self):
        return self.values['division_selection']

    def getTypeOutBread(self):
        return self.values['type_outbread']

    def getPropabilityOutBread(self):
        return self.values['propability_outbread']

    def getTypeMarginMutation(self):
        return self.values['type_margin_mutation']

    def getPropabilityMarginMutation(self):
        return self.values['propability_margin_mutation']

    def getPropabilityInversion(self):
        return self.values['PropabilityInversion']

    def getElityStartegy(self):
        '''Returning int look at SettingsConst.'''
        if self.values['radio_elity_startegy_ch1']:
            return VAL_ELITY_STRATEGY_PERCENT
        elif self.values['radio_elity_startegy_ch2']:
            return VAL_ELITY_STRATEGY_AMOUNT

    def getElityPercent(self):
        return self.values['elity_strategy_percent']

    def getElityAmount(self):
        return self.values['elity_strategy_amount']
