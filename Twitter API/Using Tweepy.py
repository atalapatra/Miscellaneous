""" 
Useful Resources:
http://docs.tweepy.org/en/v3.5.0/getting_started.html 
https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25
http://docs.tweepy.org/en/latest/
"""

import tweepy
import json
import pandas as pd

connections = json.load(open('C:/Users/amitt/OneDrive/Code/2020-07-29 Twitter API Keys/connection.json'))
api_key = connections['Twitter API']['API Key']
api_secret_key = connections['Twitter API']['API Secret Key']
bearer_token = connections['Twitter API']['Bearer Token']
access_token = connections['Twitter API']['Access Token']
access_token_secret = connections['Twitter API']['Access Token Secret']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)

public_tweets = pd.DataFrame(public_tweets)
public_tweets.iloc(1)