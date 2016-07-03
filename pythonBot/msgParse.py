# -*- coding: utf-8 -*-
import live_api
import re
import logging
import wagenreihung

log = logging.getLogger(__name__)

ZUGTYPEN=['ICE','IC','EC','RJ','TGV','CNL','AZ','D','HKX','RE','RB','IRE','S','DPN','THA', 'EN']

WAGEN_QUERYS=[re.compile('Wagen\s*(\d+)', flags=re.IGNORECASE),
              re.compile('Wg\.\s*(\d+)', flags=re.IGNORECASE),
              re.compile('\s+(\d+)', flags=re.IGNORECASE)]

ZUGNR_QUERYS=[ '^#?(%s)\s*(\d+)', '\s#?(%s)\s*(\d+)']
def parseMsg(msg):
    log.info('msg=\"'+msg+'\"')
    msg=msg.strip()
    m=False

    zugArt=None
    zugNr=None
    for zType in ZUGTYPEN:
        if m: 
            pass
        else:
            for regExPat in ZUGNR_QUERYS:
                if m: 
                    pass
                else:
                    regEx=regExPat % (zType)
                    zTypeQuery = re.compile(regEx, flags=re.IGNORECASE)
                    m = zTypeQuery.search(msg)
                    if (m):
                        zugArt=m.group(1).upper()
                        zugNr=m.group(2)
                        msg = zTypeQuery.sub('', msg,1)

    waggonNr = None
    m=False
    for query in WAGEN_QUERYS:
        if m:
            pass
        else:
            m=query.search(msg)
            if m:
                waggonNr=m.group(1)
                msg = query.sub('', msg)

    bahnhof = msg.strip()
    if bahnhof == '':
        bahnhof = None
    return (zugArt, zugNr, bahnhof, waggonNr)

def answer(msg, cnx):
    (zugArt, zugNr, bahnhof, waggonNr) = parseMsg(msg)
    return wagenreihung.anfrage(cnx, zugArt, zugNr, bahnhof, waggonNr)

