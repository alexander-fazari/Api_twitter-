#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:33:46 2020

@author: Fazari
"""

import tweepy as tw
import csv
import pandas as pd
import os
import tweepy 



#find the path of the framework
print(tw.__file__)
path = os.path.abspath(tw.__file__)
# credentials 

consumer_key = 'VOz2nKhJN5yoa5j2v4DNBTSLR'                             # API key
consumer_secret = '4rh1XdX4aoMgvvSOG3Sidjj6eQakXHjOKOhnjUuDzxOibO0zd5'  # API secret
access_token= '304341411-mwIpi5PFxns5tSI8m5R0xCSNvTJiI5a7hsTKJcdb'      # OAUTH Access token
access_token_secret = '4n4wChW6nY2J2bzjS3n5CZ8ApET2Ft9DEEHJkz3ndtXlO'    # OAUTH Access secret


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#drone"
date_since = "2020-01-01"



Tweets_DF =pd.DataFrame([])

for tweet in tweepy.Cursor(api.search,q="#drones",
                           count=100,
                           lang="en",
                           since="2017-04-03").items():
    
    print (tweet.created_at, tweet.text)
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])   
    
    Tweets_DF=Tweets_DF.append(pd.DataFrame({'user':tweet.user.screen_name ,
                                      ' Tweet':  tweet.text,
                                      ' created_at':  tweet.created_at, 
                                      
                                      },index=[0]),ignore_index=True)
    

    
    
#dataframe
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items()


 
export =  Tweets_DF.to_csv('Tweets_DF.csv') 