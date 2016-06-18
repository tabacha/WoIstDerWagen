import requests
import datetime
import config

search="EN 452"
station="Berlin HBF"

def getLiveData(search,station):

    stations=requests.get("https://open-api.bahn.de/bin/rest.exe/location.name?authKey="+config.API_KEY+"&lang=de&input="+station+"&format=json").json()
    now = datetime.datetime.now()

    station_id=stations['LocationList']['StopLocation'][0]['id']
    d=now.strftime("%Y-%m-%d")

    lastTime="00:00"
    trains=[]
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


# print(getLiveData(search,station))
