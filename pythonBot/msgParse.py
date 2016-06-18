import live_api
import re

ZUGTYPEN=['ICE','IC','EC','RJ','EN','TGV','CNL','AZ','D','HKX','RE','RB','IRE','S','DPN','THA']

LIVE_QUERYS=[re.compile('^#?([a-zA-Z]+)(\d+) (.*)$')]
WAGEN_QUERYS=[re.compile('^#?([a-zA-Z]+)(\d+) (.*) Wagen\s+(\d*)$'),
              re.compile('^#?([a-zA-Z]+)(\d+) (.*) Wg.\s+(\d*)$'),
              re.compile('^#?([a-zA-Z]+)(\d+) (.*)\s+(\d*)$')]

def abfahrt(minu):
     if (minu<0):
         return 'SEIT '+str(((-1)*minu))+' MIN. WEG'
     #else: 
     if (minu>0):
         return 'fährt in '+str(minu)+' Min. ab'
     return 'fährt jetzt ab'

def liveApiOut(rtn):
    if type(rtn)==str:
        # ERROR
        return rtn;
    else:
        # stopid
        # afahrt
        abfahrtStr=abfahrt(rtn['abfahrt'])
        if ('track' in rtn):
            return rtn['stop']+' Gleis '+rtn['track']+' Abfahrt '+ rtn['time'] + ' '+ abfahrtStr
        else:
            return rtn['stop']+' Abfahrt '+ rtn['time'] + ' '+ abfahrtStr
def answer(msg, cnx):
    print('msg=\"'+msg+'\"')
    m=False
    for query in WAGEN_QUERYS:
        if m:
            pass
        else:
            m=query.match(msg)
    if (m):
        zugArt=m.group(1)
        zugNr=m.group(2)
        bahnhof=m.group(3)
        waggonNr=m.group(4)
        print('1:'+zugArt+' '+zugNr+'\t2:'+bahnhof)
        rtn=live_api.getLiveData(zugArt+' '+zugNr, bahnhof)
        if (bahnhof.upper() == 'BERLIN'):
            cursor = cnx.cursor()
            query = cursor.execute('SELECT waggonsections FROM waggons WHERE trainname=\'%s%s\' and waggonname=\'%s\'' % (zugArt.upper(), zugNr, waggonNr))
            abschnitt=cursor.fetchone()
            if (abschnitt):
                abschnitt=abschnitt[0]
            else:
                abschnitt='unklar'
            print('XX_ABSCHNITT '+abschnitt);
            abfahrtStr=abfahrt(rtn['abfahrt'])
            return 'Bereich ' + abschnitt + ' ' + liveApiOut(rtn)
        else:                           
            return 'Nicht implementiert'
    # else:
    for query in LIVE_QUERYS:
      if m:
          pass
      else:
          m=query.match(msg)
    if m:
        zugArt=m.group(1)
        zugNr=m.group(2)
        bahnhof=m.group(3)
        print('1:'+zugArt+' '+zugNr+'\t2:'+bahnhof)
        rtn=live_api.getLiveData(zugArt+' '+zugNr, bahnhof)
        return liveApiOut(rtn)
    #  else:
    return 'Den Befehl kenne ich nicht'

