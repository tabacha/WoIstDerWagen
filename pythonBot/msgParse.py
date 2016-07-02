# -*- coding: utf-8 -*-
import live_api
import re
import logging
import wagenreihung

log = logging.getLogger(__name__)

ZUGTYPEN=['ICE','IC','EC','RJ','EN','TGV','CNL','AZ','D','HKX','RE','RB','IRE','S','DPN','THA']

LIVE_QUERYS=[re.compile('^#?([a-zA-Z]+)(\d+) (.*)$')]
WAGEN_QUERYS=[re.compile('^#?([a-zA-Z]+)(\d+) (.*) Wagen\s+(\d*)$'),
              re.compile('^#?([a-zA-Z]+)(\d+) (.*) Wg.\s+(\d*)$'),
              re.compile('^#?([a-zA-Z]+)(\d+) (.*)\s+(\d*)$')]

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
        return wagenreihung.anfrage(cnx, zugArt, zugNr, bahnhof, waggonNr)
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
        return wagenreihung.anfrage(cnx, zugArt, zugNr, bahnhof, None)
    #  else:
    return 'Den Befehl kenne ich nicht'

