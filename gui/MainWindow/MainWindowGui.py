import wx

from gui.Settings.Settings import SettingsControl


class MainFrame(wx.Frame):
    def __init__(self, parent, title, minsize=(200, 200)):
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
        # Add hello world
        self.welcomeText = wx.StaticText(self, id=wx.ID_ANY, label="Welcome on obiective wxPython", pos=(20, 150))

        self.drawSettingsButton()

    def drawSettingsButton(self):
        button = wx.Button(parent=self, label="Click me!! Please!!! ☺", pos=(20, 20))
        button.Bind(wx.EVT_BUTTON, self.onClickSettingsButton)

    def onClickSettingsButton(self, event):
        self.settingswindow.showWindow()