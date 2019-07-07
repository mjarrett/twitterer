#!/usr/bin/env python3

import tweepy
import json
import os

credfile = f"{os.path.dirname(__file__)}/twitterer/credentials.json"

with open(credfile,'r') as f:
    credentials = json.load(f)

auth = tweepy.OAuthHandler(credentials['api_key'], credentials['api_secret_key'])

redirect_url = auth.get_authorization_url()

print(redirect_url)

verifier = input('Verifier:')

auth.get_access_token(verifier)
username = auth.get_username()
access_token = auth.access_token
access_token_secret = auth.access_token_secret

credentials[username] = {'access_token':access_token
                              ,'access_token_secret':access_token_secret}

with open(credfile,'w') as f:
    json.dump(credentials,f)




