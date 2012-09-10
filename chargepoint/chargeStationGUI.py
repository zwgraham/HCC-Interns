#! /usr/bin/env python
# A GUI that searches for charge stations for electric cars
# by Conor Kaminer
# with Swag Style by ZWG



import wx
import logging
import ChargePoint
class ChargePointLocator(wx.App):
    '''
    wxPython interface to the ChargePoint netowrks location services api
    '''
    def __init__(self,key,pw, *args, **kwargs):
        wx.App.__init__(self,*args, **kwargs)
        self.key=key
        self.pw=pw

    def OnInit(self):
        frame=StationSearch(key,pw,parent=None)
        self.SetTopWindow=frame
        frame.Show()
        return 1

class SearchParameters(wx.Panel):
    '''
    panel containing search options
    '''
    def __init__(self,parent,*args,**kwargs):
        wx.Panel.__init__(self,*args,**kwargs)


class SearchResults(wx.Panel):
    '''
    panel for search results
    '''
    def __init__(self,parent,*args,**kwargs):
        wx.Panel.__init__(self,*args,**kwargs)


class Buttons(wx.Panel):
    '''
    panel for the control buttons
    '''
    def __init__(self,parent,*args,**kwargs):
        wx.Panel.__init__(self,*args,**kwargs)


class StationSearch(wx.Frame):
    '''
    window for searching for chargers
    '''
    def __init__(self, parent,key,pw, *args, **kwargs):
        wx.Frame.__init__(self, parent, title="ChargePoint Locator", size=(400,400), *args, **kwargs)
        self.parent=parent
        self.logger=logging.getLogger('ChargePointLocator')
        self.logger.debug('Building UI')
        MenuBar  = wx.MenuBar()
        FileMenu = wx.Menu()
        item = FileMenu.Append(wx.ID_EXIT, text='&Quit')
        self.Bind(wx.EVT_MENU, self.OnQuit, item)
        MenuBar.Append(FileMenu, "&File")
        self.SetMenuBar(MenuBar)

        self.StationInformation= ChargePoint.StationInformation(key,pw)
        

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
                                                                                                
    c=ChargePointLocator(0, key,pw)
    c.MainLoop()


