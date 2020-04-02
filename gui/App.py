import wx

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
        print("handled")
        self.refreshSetData()

    def refreshSetData(self):
        self.frame.panel.updateVarsBox()

