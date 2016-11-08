import requests
import datetime
import config
import logging
import json

log = logging.getLogger(__name__)

search="EC x8"
station="karlsruhe"
def findTrain(search,trains):
    now = datetime.datetime.now()
    for train in trains:
        if(train['name']==search):
            train["abfahrt"]=(int(train['time'][:2])*60+int(train['time'][3:]))-(now.hour*60+now.minute)
            train["details"]=requests.get(train["JourneyDetailRef"]["ref"]).json()
            return train

def getLiveData(search, station):
    search=search.upper()
    if (station is None):
        log.error("Keine Station in der Anfrage gefunden")
        return "Keine Station in der Anfrage gefunden"
    url="https://open-api.bahn.de/bin/rest.exe/location.name?authKey="+config.API_KEY+"&lang=de&input="+station+"&format=json"
    log.debug('get %s '%url)
    try:
        antwort=requests.get(url)
    #print(stations)
    except:
        log.error("API Fehler: %s " % url)
        return "API Fehler"
    try:
        stations=antwort.json()
    except:
        log.error("API Format Fehler, kein JSON %s " % antwort)
        return "API Format Fehler"
    now = datetime.datetime.now()
    try:
        station_id=stations['LocationList']['StopLocation'][0]['id']
        station_name=stations['LocationList']['StopLocation'][0]['name']
    except:
        log.error("Keine Station_id / name von der Live API gefunden %s JSON: %s" % (url, json.dumps(stations)))
        return "Keine Station von der Live API gefunden"
    d=now.strftime("%Y-%m-%d")

    trains=[]
    lastTime="00:00"
    while True:
        url="https://open-api.bahn.de/bin/rest.exe/departureBoard?authKey="+config.API_KEY+"&lang=de&id="+station_id+"&date="+d+"&time="+lastTime+"&format=json"
        log.debug('%s'%url)
        trains_current=requests.get(url)
        #print(trains_current.json())
        if('Departure' in trains_current.json()['DepartureBoard']):
            trains=trains+trains_current.json()['DepartureBoard']['Departure']
        #    print(trains[len(trains)-1]['time'])
            if(trains[len(trains)-1]['time'][:2]<lastTime[:2]):
                break
            else:
                lastTime=trains[len(trains)-1]['time']

    train=findTrain(search,trains)
    if(train):
        return train#just in case it is an end station
    trains=[]
    lastTime="00:00"
    while True:
        url="https://open-api.bahn.de/bin/rest.exe/arrivalBoard?authKey="+config.API_KEY+"&lang=de&id="+station_id+"&date="+d+"&time="+lastTime+"&format=json"
        log.debug("%s"%url)
        trains_current=requests.get(url)
        if('Arrival' in trains_current.json()['ArrivalBoard']):
            trains=trains+trains_current.json()['ArrivalBoard']['Arrival']
            log.debug('time %s' % trains[len(trains)-1]['time'])
            if(trains[len(trains)-1]['time'][:2]<lastTime[:2]):
                break
            else:
                lastTime=trains[len(trains)-1]['time']

    train=findTrain(search,trains)
    if(train):
        return train
    return "Zug "+search+ " konnte am Bahnhof "+station_name+" nicht gefunden werden."

    #print(trains)


#print(getLiveData(search,station))
