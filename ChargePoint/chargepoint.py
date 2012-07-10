#!/usr/bin/env python
from suds.client import Client
from suds.wsse import Security, UsernameToken


class ChargePointAPIAccount(object):
    '''
    Account Information
    '''
    def __init__(self, key, pw, url):
        self.client=Client(url)
        self.security=Security()
        self.security.tokens.append(UsernameToken(key,pw))
        self.client.set_options(wsse=self.security)


class StationInformation(ChargePointAPIAccount):
    '''
    Access the ChargePoint Network Station Information API
    '''
    def __init__(self, key, pw):
        url='https://webservices.chargepointportal.net:8081/coulomb_api_1.1.wsdl'
        ChargePointAPIAccount.__init__(self,key,pw,url)
    
    def getUSStationInformation(self, Name=None, Address=None, City=None, State=None, PostalCode=None, Lat=None, Long=None, ProximityUnit='M'):
        pass



if __name__ == "__main__":
    import ConfigParser
    try:
        Config = ConfigParser.ConfigParser()
        Config.read('./hcc.conf')
        key=Config.get('Account', 'key')
        pw=Config.get('Account', 'password')
#        url=Config.get('Account', 'url')
    except:
        print "Exception parsing config file"

    s=StationInformation(key,pw)
