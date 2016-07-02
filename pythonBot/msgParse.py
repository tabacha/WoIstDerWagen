# -*- coding: utf-8 -*-
import live_api
import re
import logging

log = logging.getLogger(__name__)

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
        gleisStr=''
        if ('track' in rtn):
             gleisStr=' Gleis '+rtn['track']
        return rtn['stop']+gleisStr+' Abfahrt '+ rtn['time'] + ' '+ abfahrtStr

def answer(msg, cnx):
    log.info('msg=\"'+msg+'\"')
    msg=msg.strip()
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
        log.debug('1:'+zugArt+' '+zugNr+'\t2:'+bahnhof)
        rtn=live_api.getLiveData(zugArt+' '+zugNr, bahnhof)
        if type(rtn) == str:
             # Fehler:
             log.error('Fehler von LiveApi %s' % rtn)
             return rtn
        cursor = cnx.cursor()
        sql='SELECT w.sections, t.additional_text FROM trains t, stations s, waggons w WHERE '
        sql=sql+'s.eva_id=%s and s.id=t.station_id  and t.number="%s" and w.train_id=t.id and w.number=%s' % (rtn['stopid'], zugNr, waggonNr)
        query = cursor.execute(sql)
        add_txts={}
        for (sections, add_txt) in cursor:
             if sections in add_txts:
                  add_txts[sections]=add_txts[sections]+' oder '+add_txt
             else:
                  add_txts[sections]=add_txt
        if len(add_txts)==1:
             return 'Bereich ' + list(add_txts.keys())[0] + ' ' + liveApiOut(rtn)
        if len(add_txts)==0:
             return 'Bereich unklar ' + liveApiOut(rtn)
        antwort='Bereich '
        for key in add_txts.keys():
             antwort=antwort+'%s (%s) ' % (key,add_txts[key])
        return antwort + liveApiOut(rtn)
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
        log.info('Art %s Nr: %s Bhf %s' % (zugArt,zugNr,bahnhof))
        rtn=live_api.getLiveData(zugArt+' '+zugNr, bahnhof)
        return liveApiOut(rtn)
    #  else:
    return 'Den Befehl kenne ich nicht'

