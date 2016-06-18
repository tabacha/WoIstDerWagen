import requests
import datetime
import config

search="ICE 375"
station="Basel SBB"

def getLiveData(search,station):

    stations=requests.get("https://open-api.bahn.de/bin/rest.exe/location.name?authKey="+config.API_KEY+"&lang=de&input="+station+"&format=json").json()
    now = datetime.datetime.now()
    #print(stations)
    station_id=stations['LocationList']['StopLocation'][0]['id']
    station_name=stations['LocationList']['StopLocation'][0]['name']
    d=now.strftime("%Y-%m-%d")

    trains=[]
    lastTime="00:00"
    while True:
        trains_current=requests.get("https://open-api.bahn.de/bin/rest.exe/departureBoard?authKey="+config.API_KEY+"&lang=de&id="+station_id+"&date="+d+"&time="+lastTime+"&format=json")
        trains=trains+trains_current.json()['DepartureBoard']['Departure']
    #    print(trains[len(trains)-1]['time'])
        if(trains[len(trains)-1]['time'][:2]<lastTime[:2]):
            break
        else:
            lastTime=trains[len(trains)-1]['time']
    for train in trains:
        if(train['name']==search):
            return train
    #just in case it is an end station
    lastTime="00:00"
    while True:
        trains_current=requests.get("https://open-api.bahn.de/bin/rest.exe/arrivalBoard?authKey="+config.API_KEY+"&lang=de&id="+station_id+"&date="+d+"&time="+lastTime+"&format=json")
        trains=trains+trains_current.json()['ArrivalBoard']['Arrival']
    #    print(trains[len(trains)-1]['time'])
        if(trains[len(trains)-1]['time'][:2]<lastTime[:2]):
            break
        else:
            lastTime=trains[len(trains)-1]['time']

    #print(trains)
    for train in trains:
        if(train['name']==search):
            return train
    return "Zug "+train+ " konnte am Bahnhof "+station_name+" nicht gefunden werden."

#print(getLiveData(search,station))
