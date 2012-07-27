#! /usr/bin/env python
# A GUI that searches for charge stations for electric cars
# by Conor Kaminer



import wx
import ChargePoint

class ChargeStationFind(wx.Frame):

	def __init__(self, parent, title):
		super(ChargeStationFind, self).__init__(parent, title=title, size = (260,180))
		self.InitUI()

	def InitUI(self):
		toolbar = self.CreateToolBar()
		exitpng = wx.Bitmap('texit.png')
		exitpng.SetSize((10,10))
		qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))
		toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

		panel = wx.Panel(self, -1)
		menubar = wx.MenuBar()
		filem = wx.Menu()
		editm = wx.Menu()
		helpm = wx.Menu()

		menubar.Append(filem, '&File')
		menubar.Append(editm, '&Edit')
		menubar.Append(helpm, '&Help')
		self.SetMenuBar(menubar)

		wx.TextCtrl(self)

		self.Centre()
		self.Show(True)
		

	def OnQuit(self, e):
		self.Close()

def main():
	ex = wx.App()
	ChargeStationFind(None, title='Charge Station Finder')
	ex.MainLoop()

if __name__ == '__main__':
	
	main()
