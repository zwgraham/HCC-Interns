#! /usr/bin/env python
# A GUI that searches for charge stations for electric cars
# by Conor Kaminer



import wx
import ChargePoint

class ChargeStationFind(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(ChargeStationFind, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		toolbar = self.CreateToolBar()
		exitpng = wx.Bitmap('texit.png')
		exitpng.SetSize((20,20))
		qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))
		toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)
		self.SetSize((500,250))
		self.SetTitle('Charge Station Finder')
		self.Show(True)
		

	def OnQuit(self, e):
		self.Close()

def main():
	ex = wx.App()
	ChargeStationFind(None)
	ex.MainLoop()

if __name__ == '__main__':
	
	main()
