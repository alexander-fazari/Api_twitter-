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


# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
    


# Collect a list of tweets
tweets = tw.Cursor(api.search,
          q=search_words,
          lang="en",
          since=date_since).items()
tweet_text=[tweet.text for tweet in tweets] 
tweet_text  
    
    
    #user  
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
   
users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
users_locs 

#dataframe
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items()

users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text,tweet.created_at] for tweet in tweets]
tweet_texts = pd.DataFrame(data=users_locs, columns=['user', "location" , "Text", "Time"])


#################################################################################################
# Create tracklist with the words that will be searched for
tracklist = ['#Brexit', '#brexit', '#br']
# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 10

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):
      
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        if tweet_count < n_tweets:
            print(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)



# Handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=tracklist)
################################################à##############################################

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since="2019-01-30",
                  ).items(100)

users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text,tweet.created_at] for tweet in tweets]
tweet_texts = pd.DataFrame(data=users_locs, columns=['user', "location" , "Text", "Time"])

    
    
#########################################àààààààààà
   
import tweepy
import datetime
import xlsxwriter
import sys

# credentials from https://apps.twitter.com/
consumerKey = "CONSUMER_KEY"
consumerSecret = "CONSUMER_SECRET"
accessToken = "ACCESS_TOKEN"
accessTokenSecret = "ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

username = sys.argv[1]
startDate = datetime.datetime(2014, 6, 1, 0, 0, 0)
endDate =   datetime.datetime(2015, 1, 1, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook(username + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")

######################################################################

import tweepy
import csv
import codecs
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#Access tokens
auth = tweepy.auth.OAuthHandler('Ro2X5OofQqS5bDU9ffK06BPHD', 'mpnQdhrwKtqw61hx5POfx2vh1VtqeUl3QmOHFWA0kTJ8X8lBmw')
auth.set_access_token('1007633217657229313-XwgX60tYA9e3eWKmEOQLhMqRl50Neo', 'Vk2YgaOGckgaMX5MBzbjySyMjh3h5fegzGDMSJ86oylRe')
api = tweepy.API(auth)
# Open/Create a file to append data
csvFile = open('result1234.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
#e=csvFile.encode('abc.csv')
f = codecs.open('abc.csv',encoding='utf-8', mode='a')
for tweet in tweepy.Cursor(api.search,
q="cool",
since="2015-01-30",
until="2015-02-01",
lang="en").items(100):
#Write a row to the csv file/ I use encode utf-8
print(tweet);
csvWriter.writerow([tweet])
    
 ################################################♣à
#working for only one week 
# Open/Create a file to append data
# csvFile = open('ua.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)

Tweets_DF =pd.DataFrame([])

for tweet in tweepy.Cursor(api.search,q="#mina",
                           count=20,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])   
    
    Tweets_DF=Tweets_DF.append(pd.DataFrame({'user':tweet.user.screen_name ,
                                      ' Tweet':  tweet.text,
                                      ' created_at':  tweet.created_at, 
                                      
                                      },index=[0]),ignore_index=True)
    
type(csvFile)
    
    
   #dataframe
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items()

users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text,tweet.created_at] for tweet in tweets]
tweet_texts = pd.DataFrame(data=users_locs, columns=['user', "location" , "Text", "Time"])
 
    export =  Tweets_DF.to_csv('Tweets_DF.csv') 
 ############################################################à
import tweepy
import csv
import pandas as pd
import sys

# API credentials here
consumer_key = 'INSERT CONSUMER KEY HERE'
consumer_secret = 'INSERT CONSUMER SECRET HERE'
access_token = 'INSERT ACCESS TOKEN HERE'
access_token_secret = 'INSERT ACCESS TOKEN SECRET HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Search word/hashtag value 
HashValue = "#drones"

# search start date value. the search will start from this date to the current date.
StartDate = "2019-12-01"

# getting the search word/hashtag and date range from user
HashValue = input("#drone")
StartDate = input("2019-12-01 ")

# Open/Create a file to append data
csvFile = open(HashValue+'.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=HashValue,count=20,lang="en",since=StartDate, tweet_mode='extended').items():
    print (tweet.created_at, tweet.full_text)
    csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])

print ("Scraping finished and saved to "+HashValue+".csv")
    
######################################################################à    
#home tweter jason  
import json 

public_tweets = api.home_timeline()

status = public_tweets[0]


#convert to string
json_str = json.dumps(status._json)

#deserialise string into python object
parsed = json.loads(json_str)

print(json.dumps(parsed, indent=4, sort_keys=True))