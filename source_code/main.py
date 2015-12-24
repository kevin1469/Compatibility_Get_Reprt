import wx
from get_issue import MyFrame

class Prob(wx.App):
  def OnInit(self):
    self.m_frame = MyFrame(None)
    self.m_frame.Show()
    self.SetTopWindow(self.m_frame)
    return True
    
app = Prob(0)
app.MainLoop()
