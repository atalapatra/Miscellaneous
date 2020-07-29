""" 
Useful Resources:
http://docs.tweepy.org/en/v3.5.0/getting_started.html 
https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25
"""

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
