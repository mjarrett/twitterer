import tweepy
import json
import datetime
import os

def tweet(user='1710_13',text='test string',media=None,in_reply_to_status_id=None):
    
    
    # initialize api
    api = get_api(user)
    
    if media is not None:
        media_ids = [api.media_upload(x).media_id for x in media]
    else:
        media_ids = None
        
    status = api.update_status(text, media_ids=media_ids, in_reply_to_status_id=in_reply_to_status_id)
    return status


def get_api(user='1710_13'):
    #Authorize user
    with open(f'{os.path.dirname(__file__)}/credentials.json','r') as f:
        credentials = json.load(f)

    auth = tweepy.OAuthHandler(credentials['api_key'], credentials['api_secret_key'])
    auth.set_access_token(credentials[user]['access_token'], credentials[user]['access_token_secret'])

    # initialize api
    api = tweepy.API(auth)
    return api


def warning(s):
    try:
        tweet('1710_13',f"@mikejarrett_ {s} {datetime.datetime.now()}")
    except Exception as e:
        print(e)
              
def get_tweet(tweet_id):
    api = get_api()

    return api.get_status(tweet_id)

def list_users():
    with open(f'{os.path.dirname(__file__)}/credentials.json','r') as f:
        credentials = json.load(f)
    for user in credentials.keys():
        print(user)
        