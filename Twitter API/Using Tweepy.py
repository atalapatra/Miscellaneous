""" 
Useful Resources:
http://docs.tweepy.org/en/v3.5.0/getting_started.html 
https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25
http://docs.tweepy.org/en/latest/

Creating The Twitter Sentiment Analysis Program in Python with Naive Bayes Classification
https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed
"""

import tweepy
import json
import pandas as pd

## Functions

def buildTestSet(search_keyword):
    try:
        tweets_fetched = api.GetSearch(search_keyword, count = 100)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None

## Analysis

connections = json.load(open('C:/Users/amitt/OneDrive/Code/2020-07-29 Twitter API Keys/connection.json'))
api_key = connections['Twitter API']['API Key']
api_secret_key = connections['Twitter API']['API Secret Key']
bearer_token = connections['Twitter API']['Bearer Token']
access_token = connections['Twitter API']['Access Token']
access_token_secret = connections['Twitter API']['Access Token Secret']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# # Test that Twitter API connection is working
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (f"{tweet.user.name}: {tweet.text}")
# 
# public_tweets = pd.DataFrame(public_tweets)
    
search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])

tweets_fetched = api.search("game", count = 100)

