#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, pprint, config
from mysql.connector import (connection) 
import msgParse

cnx = connection.MySQLConnection(user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, host= config.MYSQL_HOST, database=config.MYSQL_DB)
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)
myLastTweet = api.me().timeline(count=1)
pp = pprint.PrettyPrinter(indent=2);
while True:
    print('ask twitter for new tweets')
    mentions = api.mentions_timeline(since_id=myLastTweet[0].id)
    for mention in mentions:
        print(mention.author.screen_name, '\t', mention.text)
        question=mention.text.replace('@WoIstDerWagen ', '')
        txt='@' + mention.author.screen_name + ' ' + msgParse.answer(question, cnx)
        print('Antwort an Twitter: '+txt)
        api.update_status(txt,mention.id)
        myLastTweet = api.me().timeline(count=1)
    time.sleep(120)
cnx.close()
