import live_api
import re

LIVE_QUERY=re.compile('^([a-zA-Z]+)(\d+) (.*)$')
def answer(msg, cnx):
    m=LIVE_QUERY.match(msg)
    if (m):
        zugArt=m.group(1)
        zugNr=m.group(2)
        bahnhof=m.group(3)
        print('1:'+zugArt+' '+zugNr+'\t2:'+bahnhof)
        rtn=live_api.getLiveData(zugArt+' '+zugNr, bahnhof)
        return 'Der Zug fährt auf Gleis '+rtn['track']+' Abfahrt '+ rtn['time']
    else:
        return 'Den Befehl kenne ich nicht'

