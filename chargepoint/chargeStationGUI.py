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
		#toolbar = self.CreateToolBar()
		#exitpng = wx.Bitmap('texit.png')
		#exitpng.SetSize((10,10))
		#qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))
		#toolbar.Realize()
		#self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

		panel = wx.Panel(self)

		hbox = wx.BoxSizer(wx.HORIZONTAL)

		fgs = wx.FlexGridSizer(3,2,9,25)
		
		addressTxt = wx.StaticText(panel, label="Address")
		zipCodeTxt = wx.StaticText(panel, label="Zip Code")

		textbox1 = wx.TextCtrl(panel)
		textbox2 = wx.TextCtrl(panel)

		fgs.AddMany([(addressTxt), (textbox1, 1, wx.EXPAND), (zipCodeTxt), (textbox2, 1, wx.EXPAND)])

		fgs.AddGrowableRow(2,1)
		fgs.AddGrowableCol(1,1)

		hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
		panel.SetSizer(hbox)

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
