#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, pprint, config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)
myLastTweet = api.me().timeline(count=1)
pp = pprint.PrettyPrinter(indent=2);
#pp.pprint(myLastTweet)
mentions = api.mentions_timeline(since_id=myLastTweet[0].id)
for mention in mentions:
    
    print(mention.text)
    print(mention.author.screen_name)
    txt='@' + mention.author.screen_name + ' Den Befehl kenne ich noch nicht'
    api.update_status(txt) 
