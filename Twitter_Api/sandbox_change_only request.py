
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

# parameter for the full
search_params = {
    'query': '#drones',
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    'fromDate':'201802010000', 
    'toDate':'201802282359' ,
    # 'maxResults' :100
    'next':'eyJtYXhJZCI6OTY4OTg3NTc0MzA2OTcxNjQ4fQ=='
}

# parameter for the 30
search_params = {
    'query': '#drones',
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    # 'fromDate':'201802010000', 
    # 'toDate':'201802282359' ,
    'maxResults' :100
}


# for the standard 
search_params = {
    'q': '#drones',
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    # 'fromDate':'201802010000', 
    # 'toDate':'201802282359' ,
    'maxResults' :100
}


# works only with query q and other parameters 
search_url = '{}1.1/search/tweets.json'.format(base_url)
# check parameters 
search_url = '{}1.1/tweets/search/30day/NLP.json'.format(base_url)


# full archive 
search_url = '{}1.1/tweets/search/fullarchive/NLP.json'.format(base_url)


search_url='https://api.twitter.com/1.1/tweets/search/fullarchive/NLP.json'

search_resp = requests.get(search_url, headers=search_headers, params=search_params)


 # search_resp  = requests.post('https://api.twitter.com/1.1/tweets/search/fullarchive.json', headers=search_headers, params=search_params)


tweet_data = search_resp.json()
search_resp.status_code


# this for the data of standard 
for x in tweet_data['statuses']:
    print(x['text'] + '\n')
    
    
    
    # this for the data of 30 and fuòll
    
    for x in tweet_data['results']:
    print(x['text'] + '\n')
    # what to do is to take the next from the tweet data and put in the request '{}:{}'.format5
    tweet_data['next']
    
    # trend near location 
    search_params = {
     
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    # 'fromDate':'201802010000', 
    # 'toDate':'201802282359' ,
    'id':'1'
}

    
    search_url ='https://api.twitter.com/1.1/trends/place.json'
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
      # trend near lat lang 
      search_params = {
     'lat':'45.0703',
     'long':'7.6869'
    # 'result_type': 'recent',
    # 'count': 2,
     # 'maxResults': '100',
    # 'fromDate':'201802010000', 
    
}

    
    search_url ='https://api.twitter.com/1.1/trends/closest.json'
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    
     
    
    