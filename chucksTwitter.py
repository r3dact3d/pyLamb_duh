#!/usr/bin/env python
# written by r3dact3d (brady)
import requests
import tweepy
import os
import boto3
from random import choice

'''
Chucknorris.io is free and will always be! However, as maintaining this service costs $$$,
we are glad to be sponsored by Jugendstil.io.
'''

def tweet(api, payLoad):
    try:
        if payLoad != '\n':
            api.update_status(payLoad)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)

def lambda_handler(event, context):
    # Available Catagories - I did this way so specific catagories could be removed if you want... but chuck would not approve.
    chuckagories = ["explicit", "dev", "movie", "food", "celebrity", "science", "sport", "political", "religion", "animal", "history", "music", "travel", "career", "money", "fashion"]
    chuckagory = choice(chuckagories)
    url = 'https://api.chucknorris.io/jokes/random'

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
    myParams = {
    'query' : chuckagories,
    }
    page = requests.get(url, params=myParams)
    if page.status_code == 200:
        output = page.json()
        chuckSays = output['value']
        payLoad = '#chucknorris "%s"' % (chuckSays[:125])
        tweet(api, payLoad)
    else:
        print('Something went wrong with the API, someone is in big trouble if Chuck finds out!')
        exit()
