import live_api
import re

ZUGTYPEN=['ICE','IC','EC','RJ','EN','TGV','CNL','AZ','D','HKX','RE','RB','IRE','S','DPN','THA']

LIVE_QUERYS=[re.compile('^#?([a-zA-Z]+)(\d+) (.*)$')]
WAGEN_QUERYS=[re.compile('^#?([a-zA-Z]+)(\d+) (.*) (\d*)$'),
              re.compile('^#?([a-zA-Z]+)(\d+) (.*) Wg. \s+(\d*)$'),
              re.compile('^#?([a-zA-Z]+)(\d+) (.*) Wagen \s+(\d*)$')]

def answer(msg, cnx):
    print('msg=\"'+msg+'\"')
    m=False
    for query in WAGEN_QUERYS:
        if m:
            pass
        else:
            m=query.match(msg)
    if (m):
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
        if type(rtn)==str:
            # ERROR
            return rtn;
        else:
            # stopid
            # afahrt
            abfahrt='fährt jetzt ab'
            if (rtn['abfahrt']<0):
                'SEIT '+str(((-1)*rtn['abfahrt']))+' MIN. WEG'
            else: 
                if (rtn['abfahrt']>0):
                    'fährt in '+str(rtn['abfahrt'])+' Min. ab'
            return rtn['stop']+' Gleis '+rtn['track']+' Abfahrt '+ rtn['time']
    #  else:
    return 'Den Befehl kenne ich nicht'

