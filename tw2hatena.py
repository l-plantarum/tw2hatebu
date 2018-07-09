import json, sys, config, re
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
tw = OAuth1Session(CK, CS, AT, ATS)

baseurl = "https://api.twitter.com/1.1"
favorites_url = baseurl + "/favorites/list.json"
tweet_url = baseurl + "/search/tweets.json"

def getFavorites(name):
	res = tw.get(favorites_url, params = { 'screen_name': name })
	tweets = json.loads(res.text)
	return tweets 

def getTweets(name):
	res = tw.get(tweet_url, params = { 'q': "from:" + name })
	tweets = json.loads(res.text)
	return tweets 

def expandURL(url):
	conn = http.client.HTTPSConnection("t.co")
	conn.rquest("GET", url)
	res = conn.getresponse()
	if res.status == 301:
		hdr = res.getheader("location")
		return hdr
	else:
		return None

def getURL(tw):
	if tw in "https://t.co/":
		url = re.findall("https://t.co/[A-Za-z0-9]", tw)
		return expandURL(url)
	else:
		return None
	

# ふぁぼったURLをブクマ
entries = getFavorites(sys.argv[1])

for item in entries:
    tw = item['text']
    url = getUrl(tw)
    if url != None:
        bookmark(url, "")


# RT/tweetしたURLをブクマ
entries = getTweets(sys.argv[1])

results = entries['statuses']
for item in results:
    tw = item['text']
    url = getUrl(tw)
    if url != None:
        bookmark(url, tw)
