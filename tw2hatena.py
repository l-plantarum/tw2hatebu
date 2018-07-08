import json, sys, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
tw = OAuth1Session(CK, CS, AT, ATS)

baseurl = "https://api.twitter.com/1.1"
favorites_url = baseurl + "/favorites/list.json"

def getFavorites(name):
	res = tw.get(favorites_url, params = { 'screen_name': name })
	tweets = json.loads(res.text)
	return tweets 

tw = getFavorites(sys.argv[1])

for item in tw:
    print(item['text'])

