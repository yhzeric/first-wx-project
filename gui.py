import wx

def OnJoshButton(e):
	print "fool"

app = wx.App(False)

frame = wx.Frame(None, wx.ID_ANY, "title")

btnJosButton = wx.Button(frame, label = "This is a button!")

btnJosButton.Bind(wx.EVT_BUTTON,OnJoshButton)

frame.Show(True)

app.MainLoop()