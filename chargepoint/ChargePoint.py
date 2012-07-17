#!/usr/bin/env python
from suds.client import Client
from suds.wsse import Security, UsernameToken
import logging

module_logger = logging.getLogger('ChargePoint')

class ChargePointAPIAccount(object):
    '''
    Account Information
    '''
    def __init__(self, key, pw, url):
        self.logger=logging.getLogger('ChargePoint.ChargePointAPIAccount')
        self.client=Client(url)
        self.security=Security()
        self.security.tokens.append(UsernameToken(key,pw))
        self.client.set_options(wsse=self.security)


class StationInformation(ChargePointAPIAccount):
    '''
    Access the ChargePoint Network Station Information API
    '''
    def __init__(   self, key, pw,
                    url='https://webservices.chargepointportal.net:8081/coulomb_api_1.1.wsdl'):
        ChargePointAPIAccount.__init__(self,key,pw,url)

    def SearchByZipCode(self, ZipCode='93906', Proximity=15, ProximityUnit='M'):
        self.logger.info('Searching by Zipcode(%s)'%(ZipCode))
        searchRequest = self.client.factory.create('stationSearchRequest')
        searchRequest.postalCode=ZipCode
        searchRequest.Proximity=Proximity
        searchRequest.proximityUnit=ProximityUnit
        reply=self.client.service.getAllUSStations(searchRequest)
        self.logger.debug('API returned code %{0}'.format(reply.responseCode))
        #needs error checking by response code
        stationsInZipCode=[]
        for station in reply.stationData:
            if station.postalCode == ZipCode:
                stationsInZipCode.append(station)
        self.logger.info('API Returned %d results %d of which were in %s'%(len(reply.stationData),len(stationsInZipCode),ZipCode))
        return stationsInZipCode

    def SearchByGeo(self, Latitude='36.673192', Longitude = '-121.605089', Proximity=20, ProximityUnit='M'):
        self.logger.info('Searching by GPS(%s,%s)'%(Latitude,Longitude))
        searchRequest = self.client.factory.create('stationSearchRequest')
        searchRequest.Geo.lat=Latitude
        searchRequest.Geo.long=Longitude
        searchRequest.Proximity=Proximity
        searchRequest.proximityUnit=ProximityUnit
        reply=self.client.service.getAllUSStations(searchRequest)
        self.logger.debug('API returned code %s: $s'%(reply.responseCode,reply.responseText))
        #needs error checking by response code
        stationsByGeo=[]
        #can't we just return reply.stationData?
        #either "return reply.stationData" or "stationsByGeo=reply.stationData"
        for station in reply:
            stationsByGeo.append(station)
        self.logger.info('API Returned %d results'%(len(stationsByGeo)))
        return stationsByGeo
    
    def searchByAddress(self, Address='1743 East Alisal St', City='Salinas', State='CA', Proximity=15, ProximityUnit='M'):
        self.logger.info('Searching by address:  %s, %s %s'%(Address,City,State))
        searchRequest = self.client.factory.create('stationSearchRequest')
        searchRequest.Address = Address
        searchRequest.City= City
        searchRequest.State = State
        searchRequest.Proximity=Proximity
        searchRequest.proximityUnit=ProximityUnit
        reply=self.client.service.getAllUSStations(searchRequest)
        self.logger.debug('API returned code %d: $s'%(int(reply.responseCode),reply.responseText))
        stationByAddress = []
        #can't we just return reply.stationData?
        for station in reply.stationData:
            stationByAddress.append(station)
        self.logger.info('API Returned %d results' %(len(stationByAddress)))
        return stationByAddress


if __name__ == "__main__":
    import ConfigParser
    #logging.basicConfig(filename='debug.log')
    try:
        Config = ConfigParser.ConfigParser()
        Config.read('./hcc.conf')
    except:
    print "Exception reading config file"
    try:
        key=Config.get('Account', 'key')
        pw=Config.get('Account', 'password')
        url=Config.get('General', 'url')
    except:
        print "Exception parsing config file"
    
    s=StationInformation(key,pw)
    logging.getLogger('suds.transport').setLevel(logging.DEBUG)
    logging.getLogger('ChargePoint.ChargePointAPIAccount').setLevel(logging.DEBUG)
    print '*******'
    for l in s.SearchByZipCode('93907', '10'):
        print l.postalCode
        print '*******'
