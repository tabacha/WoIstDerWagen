import requests
import datetime
import config

search="EC x8"
station="karlsruhe"
def findTrain(search,trains):
    now = datetime.datetime.now()
    for train in trains:
        if(train['name']==search):
            train["abfahrt"]=int(train['time'][:2])*60+int(train['time'][3:])-now.hour*60+now.minute
            train["details"]=requests.get(train["JourneyDetailRef"]["ref"]).json()
            return train

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
        if(trains_current.json()['DepartureBoard']['Departure']):
            trains=trains+trains_current.json()['DepartureBoard']['Departure']
        #    print(trains[len(trains)-1]['time'])
            if(trains[len(trains)-1]['time'][:2]<lastTime[:2]):
                break
            else:
                lastTime=trains[len(trains)-1]['time']
        else:
            break
    train=findTrain(search,trains)
    if(train):
        return train#just in case it is an end station
    trains=[]
    lastTime="00:00"
    while True:
        trains_current=requests.get("https://open-api.bahn.de/bin/rest.exe/arrivalBoard?authKey="+config.API_KEY+"&lang=de&id="+station_id+"&date="+d+"&time="+lastTime+"&format=json")

        if(trains_current.json()['ArrivalBoard']['Arrival']):
            trains=trains+trains_current.json()['ArrivalBoard']['Arrival']
        #    print(trains[len(trains)-1]['time'])
            if(trains[len(trains)-1]['time'][:2]<lastTime[:2]):
                break
            else:
                lastTime=trains[len(trains)-1]['time']
        else:
            break
    train=findTrain(search,trains)
    if(train):
        return train
    return "Zug "+search+ " konnte am Bahnhof "+station_name+" nicht gefunden werden."

    #print(trains)


#print(getLiveData(search,station))
