import tweepy
from config import *

### Global Vars
techWords = ['redhat', 'red hat', 'kubernetes', 'ansible', 'tech', 'hacker', 'opensource', 'data science', 'pipeline', 'sysops', 'devops', 'automation']
query = '"call for speakers" OR "submit your talk" -filter:retweets'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def findTweet(techWords, query):
#    for tweet in tweepy.Cursor(api.search, q=query, lang='en', geocode='32.7078750,-96.9209130,100km').items(10):
    for tweet in tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items(10):
        try:
            text = tweet.retweeted_status.full_text.lower()
        except:
            text = tweet.full_text.lower()
        for word in techWords:
            if word in text:
                if not tweet.retweeted:
                    try:
                        tweet.retweet()
                        print("\tRetweeted" + text)
                    except tweepy.TweepError as e:
                        print("\tAlready Retweeted" + text)


findTweet(techWords, query)

