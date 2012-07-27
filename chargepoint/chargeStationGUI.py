#! /usr/bin/env python
# A GUI that searches for charge stations for electric cars
# by Conor Kaminer



import wx
import ChargePoint

class ChargeStationFind(wx.Frame):

	def __init__(self, parent, title):
		super(ChargeStationFind, self).__init__(parent, title=title, size = (500,400))
		self.InitUI()

	def InitUI(self):
		toolbar = self.CreateToolBar()
		exitpng = wx.Bitmap('texit.png')
		exitpng.SetSize((1,1))
		qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))
		toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

		panel = wx.Panel(self)

		fgs = wx.GridBagSizer(4,4)
		
		addressTxt = wx.StaticText(panel, label="Address")
		zipCodeTxt = wx.StaticText(panel, label="Zip Code")

		textbox1 = wx.TextCtrl(panel)
		textbox2 = wx.TextCtrl(panel)
			
		searchButton = wx.Button(panel, label="Search", size=(90,28))

		fgs.Add (addressTxt, pos=(1,1), span=(1,2), flag=wx.LEFT|wx.EXPAND)
		fgs.Add (textbox1, pos=(1,3), span=(1,3), flag=wx.RIGHT|wx.EXPAND) 
		fgs.Add(zipCodeTxt,pos=(2,1), span=(1,2), flag=wx.LEFT|wx.EXPAND) 
		fgs.Add(textbox2, pos=(2,3), span=(1,3),flag=wx.RIGHT|wx.EXPAND)
		fgs.Add(searchButton,pos=(5,5), span=(1,3), flag=wx.RIGHT)

		fgs.AddGrowableRow(3)
		fgs.AddGrowableCol(3)
		panel.SetSizerAndFit(fgs)

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
