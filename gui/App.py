import numpy as np
import wx
from matplotlib import cm

import matplotlib.pyplot as plt
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


