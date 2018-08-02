import wx

# class App(wx.App):
#     def OnInit(self):
#         frame = wx.Frame(parent=None, title="myfirst")
#         button = wx.Button(frame, label="我的天")
#         frame.Show()
#
#         return True


if __name__ == '__main__':
    a = wx.App()
    fr = wx.Frame(None, title="Hello World2")
    fr.Show()
    st = wx.StaticText(fr, label="Hello world", pos=(25, 25))
    sb=fr.CreateStatusBar()
    fr.SetStatusText("wangbo")
    a.MainLoop()
