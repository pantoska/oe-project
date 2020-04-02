import wx

from gui.MainWindow.MainWindowGui import MainFrame

class AppMain(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # handle event from child
        self.Bind(wx.EVT_BUTTON, self.SettedData)
        # init Frame
        self.InitFrame()

    def InitFrame(self):
        frame = MainFrame(None, "Funkcja jakaś tam!")
        frame.Show()

    def SettedData(self, event):
        self.refreshSettedData()

    def refreshSettedData(self):
        frame.refreshValueBox()

