#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, pprint, config
from mysql.connector import (connection) 
import msgParse
import re
import os
import logging
from daemonize import Daemonize


def init():
    global log
    global cnx
    global api
    if (hasattr(config,'logger')):
        import logging.config
        logging.config.dictConfig(config.logger)
    log = logging.getLogger(__name__)
    cnx = connection.MySQLConnection(user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, host= config.MYSQL_HOST, database=config.MYSQL_DB)
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
    api = tweepy.API(auth)



def mainProgram():
    global log
    global cnx
    global api
    log.info('Starting WoIstDerWagen Twitter bot with pid %d' % os.getpid())
    reTwitterHandle = re.compile("@WoIstDerWagen", re.IGNORECASE)
    while True:
        inReplyToStatusId = api.me().timeline(count=1)[0].in_reply_to_status_id
        log.info('ask twitter for new tweets since %d',inReplyToStatusId)
        mentions = api.mentions_timeline(since_id=inReplyToStatusId)
        if (cnx.is_connected()==False):
            log.info('mysql reconnect')
            cnx.reconnect(attempts=2, delay=10)
        for mention in reversed(mentions):
            log.info('Tweet %d from %s, Text: %s' % (mention.id, mention.author.screen_name, mention.text))
            question=reTwitterHandle.sub('', mention.text)
            txt='@' + mention.author.screen_name + ' ' + msgParse.answer(question, cnx)
            log.info('Answer to Twitter: %s' % (txt))
            try:
                while (len(txt)>139):
                    firstPart=txt[:136]+'...'
                    log.info('msg>139 chars. Splitting. msg=%s' % (firstPart))
                    api.update_status(firstPart, mention.id)
                    txt='@' + mention.author.screen_name + ' ...' +txt[136:]
                log.info('Tweet: %s' %(txt))
                api.update_status(txt,mention.id)
            except tweepy.error.RateLimitError as e:
                sleep=(60*15)-(time.time() %(60*15))
                log.exception('Twitter Rate Limit error sleep=%f' % sleep)
                time.sleep(sleep)
            except tweepy.error.TweepError as e:
                log.exception('Tweepy error')
                time.sleep(20)
            except mysql.connector.errors.OperationalError as e:
                log.exception('Mysql error')
        time.sleep(120)


init()
daemon = Daemonize(app='WoIstDerWagen', 
                   pid='/tmp/WoIstDerWagen.pid', 
                   action=mainProgram, 
                   logger=log,
                   foreground=True,
                   auto_close_fds=False)
daemon.start()

