import requests



import base64



key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')



base_url = 'https://api.twitter.com/'
base_url = 'https://api.twitter.com/oauth2/token'

auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

auth_resp.status_code

# Keys in data response are token_type (bearer) and access_token (your access token)
auth_resp.json().keys()

access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}


data = '{              "query":"from:TwitterDev lang:en",\n                "maxResults": "100",\n                "fromDate":"201802010000", \n                "toDate":"201802282359"\n                }'


search_url='https://api.twitter.com/1.1/tweets/search/fullarchive/prod.json'

search_resp = requests.get(search_url, headers=search_headers, params=data)


search_resp.status_code

tweet_data = search_resp.json()
# ... tweet_data

for x in tweet_data['statuses']:
    print(x['text'] + '\n')


########################################################
    import requests

data = {
  'grant_type': 'client_credentials'
}

response = requests.post('https://api.twitter.com/oauth2/token', data=data, auth=(API key, API secret key))
