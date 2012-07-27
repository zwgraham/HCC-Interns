#! /usr/bin/env python
# A GUI that searches for charge stations for electric cars
# by Conor Kaminer
# with Swag Style by ZWG



import wx
import logging
import ChargePoint

class ChargeStationFind(wx.Frame):
    '''
    Custom Frame for the App
    '''
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.logger=logging.getLogger('ChargeStationFrame')
        self.InitUI()

    def InitUI(self):
        self.logger.debug('Building UI')
        toolbar = self.CreateToolBar()
        exitpng = wx.Bitmap('texit.png')
        exitpng.SetSize((10,10))
        qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))
        toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)
        self.SetSize((500,250))
        self.SetTitle('Charge Station Finder')
        self.Show(True)
        

    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':
    import ConfigParser
    #logging.basicConfig(filename='debug.log')
    try:
        Config = ConfigParser.ConfigParser()
        Config.read('./hcc.conf')
    except:
        print "Exception reading config file"
        exit()
    try:
        key=Config.get('Account', 'key')
        pw=Config.get('Account', 'password')
        url=Config.get('General', 'url')
    except:
        print "Exception parsing config file"
        exit()
                                                                                                

    ex = wx.App()
    ChargeStationFind(None)
    ex.MainLoop()


