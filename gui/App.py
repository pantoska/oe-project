import wx

from gui.MainWindow.MainWindowGui import MainFrame

class AppMain(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # init Frame
        self.InitFrame()

    def InitFrame(self):
        frame = MainFrame(None, "Funkcja jakaś tam!")
        frame.Show()