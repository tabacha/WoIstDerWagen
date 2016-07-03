#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, pprint, config
from mysql.connector import (connection) 
import msgParse
import re
import os

import logging

if (hasattr(config,'logger')):
    import logging.config
    logging.config.dictConfig(config.logger)

log = logging.getLogger(__name__)
log.info('Starting WoIstDerWagen Twitter bot with pid %d' % os.getpid())

cnx = connection.MySQLConnection(user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, host= config.MYSQL_HOST, database=config.MYSQL_DB)
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)
myLastTweet = api.me().timeline(count=1)
#print(myLastTweet)
#print(myLastTweet[0].in_reply_to_status_id)
pp = pprint.PrettyPrinter(indent=2);
reTwitterHandle = re.compile("@WoIstDerWagen", re.IGNORECASE)
while True:

    mentions = api.mentions_timeline(since_id=myLastTweet[0].in_reply_to_status_id)
    if (cnx.is_connected()==False):
        log.info('mysql reconnect')
        cnx.reconnect(attempts=2, delay=10)
    log.info('ask twitter for new tweets since %d',myLastTweet[0].in_reply_to_status_id)
    for mention in mentions:
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
            api.update_status(txt,mention.id)
            myLastTweet = api.me().timeline(count=1)
            log.info('Last Tweet irts: %d', myLastTweet[0].in_reply_to_status_id)
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
cnx.close()
