#!/usr/bin/env python
# written by brady [r3dact3d]
import requests
import tweepy
import os
import boto3
import lxml
from bs4 import BeautifulSoup

url = 'http://www.urbandictionary.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")
data = dict()
data['def'] = soup(class_ = 'meaning')[0].text
data['word'] = soup(class_ = 'word')[0].text
word = data['word'].strip('u').strip('\n')
meaning = data['def'].strip('u').strip('\n')
short = 'https://goo.gl/gZMF'

payLoad = 'Daily #UrbanDictionary> %s: %s ... %s' % (word, meaning[:65], short)

# Set up OAuth and integrate with API
accessToken = os.getenv("ACCESS_TOKEN")
accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")
consumerKey = os.getenv("CONSUMER_KEY")
consumerSecret = os.getenv("CONSUMER_SECRET")
oauthParams = [accessToken, accessTokenSecret, consumerKey, consumerSecret]

ssm = boto3.client('ssm')
result = ssm.get_parameters(Names=oauthParams, WithDecryption=True)

if result['InvalidParameters']:
    raise RuntimeError('Could not find OAuth params containing Twitter API Keys: {}'.format(oauthParams))
param_lookup = {param['Name']: param['Value'] for param in result['Parameters']}   

auth = tweepy.OAuthHandler(param_lookup[consumerKey], param_lookup[consumerSecret])
auth.set_access_token(param_lookup[accessToken], param_lookup[accessTokenSecret])
api = tweepy.API(auth)

def tweet(payLoad):
    try:
        print(payLoad)
        if payLoad != '\n':
            api.update_status(payLoad)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)

def lambda_handler(event, context):
    tweet(payLoad)
