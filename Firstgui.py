import wx

from gui.Settings import SettingsControl


class MyAppMain(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # init Frame
        self.InitFrame()

    def InitFrame(self):
        frame = MyMainFrame(None, "My frame")
        frame.Show()


class MyMainFrame(wx.Frame):
    def __init__(self, parent, title, minsize=(200, 200)):
        super().__init__(parent=parent, title=title)
        self.SetMinSize(minsize)
        self.OnInit()

    def OnInit(self):
        panel = MyMainPanel(self)


class MyMainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.clickCount = 0

        # Add hello world
        self.welcomeText = wx.StaticText(self, id=wx.ID_ANY, label="Welcome on obiective wxPython", pos=(20, 150))

        # Button
        button = wx.Button(parent=self, label="Click me!! Please!!! ☺", pos=(20, 20))
        button.Bind(wx.EVT_BUTTON, self.onClickButton)

        # window
        self.settingswindow = SettingsControl(self.GetParent())

    def onClickButton(self, event):
        self.clickCount += 1
        self.welcomeText.SetLabel("Ohhh you clicked button " + str(self.clickCount) + " times!")
        self.settingswindow.showWindow()
        if 10 < self.clickCount < 12:
            dlg = wx.RichMessageDialog(None,
                                       "Oh no!! You clicked so a lot of times button!!",
                                       "You are crazy person!",
                                       wx.OK)
            dlg.ShowModal()


if __name__ == "__main__":
    app = MyAppMain()
    app.MainLoop()
