#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
#keys 
consumer_key = 'VOz2nKhJN5yoa5j2v4DNBTSLR'                             # API key
consumer_secret = '4rh1XdX4aoMgvvSOG3Sidjj6eQakXHjOKOhnjUuDzxOibO0zd5'  # API secret
access_token= '304341411-mwIpi5PFxns5tSI8m5R0xCSNvTJiI5a7hsTKJcdb'      # OAUTH Access token
access_token_secret = '4n4wChW6nY2J2bzjS3n5CZ8ApET2Ft9DEEHJkz3ndtXlO'    # OAUTH Access secret


client_key =consumer_key
client_secret= consumer_secret
import base64

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

import requests
base_url = 'https://api.twitter.com/'

auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

#check the status of the request 

auth_resp.status_code
# Keys in data response are token_type (bearer) and access_token (your access token)
auth_resp.json().keys()

access_token = auth_resp.json()['access_token']


#Make a query 

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

# parameter for the full acrive
search_params = {
    'query': '#drones',
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
     'fromDate':'201912010000', 
    'toDate':'201912312359' ,
    # 'maxResults' :100
    # 'next':'eyJtYXhJZCI6OTY4OTg3NTc0MzA2OTcxNjQ4fQ=='
}

# parameter for the 30days search 
search_params = {
    'query': '#drones',
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    # 'fromDate':'201802010000', 
    # 'toDate':'201802282359' ,
    'maxResults' :100
}


# parameters for the standard search 
search_params = {
    'q': '#drones',
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    # 'fromDate':'201802010000', 
    # 'toDate':'201802282359' ,
    'maxResults' :100
}


# standared search URL  
search_url = '{}1.1/search/tweets.json'.format(base_url)
# 30 days search URL 
search_url = '{}1.1/tweets/search/30day/NLP.json'.format(base_url)


# full archive 
search_url = '{}1.1/tweets/search/fullarchive/NLP.json'.format(base_url)
# search_url='https://api.twitter.com/1.1/tweets/search/fullarchive/NLP.json'

# Make a get request for url 

search_resp = requests.get(search_url, headers=search_headers, params=search_params)


# search_resp  = requests.post('https://api.twitter.com/1.1/tweets/search/fullarchive.json', headers=search_headers, params=search_params)



# check the response of the server if 200 its okay 
search_resp.status_code

# get the twetter in dict with the next token to be used for complete the request 

tweet_data = search_resp.json()


# this for  print the data of standard search 
for x in tweet_data['statuses']:
    print(x['text'] + '\n')
    
    

next_token=tweet_data['next']

import pandas as pd
Tweets_DF =pd.DataFrame([])
Token_list=pd.DataFrame([])

for i in range(0,10000):
    # next token 
    next_token=tweet_data['next']
    
    Tweets_DF=Tweets_DF.append(pd.DataFrame({'Token number ':i ,
                                  'token id':  next_token},index=[0]),ignore_index=True)

    
    # parameter for the full acrive
    search_params = {
    'query': '#drones',
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    'fromDate':'201912010000', 
    'toDate':'201912312359' ,
    # 'maxResults' :100
    'next':'{}'.format(next_token)}
    
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    tweet_data = search_resp.json()
    #loop and save the data 
    for n in range(0,99):
        created_at=tweet_data['results'][n]['created_at']
        text=tweet_data['results'][n]['text']
        user_id=tweet_data['results'][n]['user']['id']
        screen_name=tweet_data['results'][n]['user']['screen_name']
        user_description=tweet_data['results'][n]['user']['description']
        friends_count=tweet_data['results'][n]['user']['friends_count']
        followers_count=tweet_data['results'][n]['user']['followers_count']
        profile_created_at=tweet_data['results'][n]['user']['created_at']
        retweeted=tweet_data['results'][n]['retweeted']
        retweet_count=tweet_data['results'][n]['retweet_count']
        reply_count=tweet_data['results'][n]['reply_count']
        lang=tweet_data['results'][n]['lang']
        tweet_id=tweet_data['results'][n]['id']
        
        Tweets_DF=Tweets_DF.append(pd.DataFrame({'user_id':user_id ,
                                      ' screen_name':  screen_name,
                                      ' user_description':  user_description, 
                                      ' profile_created_at':  profile_created_at,
                                      ' user_description':  user_description, 
                                      ' friends_count': friends_count,
                                      ' followers_count':  followers_count, 
                                      ' tweet_id':  screen_name,
                                      ' retweeted':  retweeted, 
                                      ' retweet_count':  retweet_count,
                                      ' reply_count':  reply_count, 
                                      ' text':  text, 
                                      ' lang':  lang,
                                      ' tweet_created_at':  created_at
                                                                       
                                      },index=[0]),ignore_index=True)
        
        

    
    i=i+1
    print('Next token number' ,i)
    if i==29:
        time.sleep(900)
    
    
    

limit=requests.get('https://api.twitter.com/1.1/application/rate_limit_status.json?resources=help,users,search,statuses',headers=search_headers, params=None)
    
limit_json=limit.json()
    
    