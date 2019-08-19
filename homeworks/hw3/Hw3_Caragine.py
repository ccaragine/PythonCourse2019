############## Homework 3 ##############
## Crystal Caragine
## 8/16/2019
## Hw3_Caragine

## Importing packages 
import tweepy
# http://docs.tweepy.org/en/v3.8.0/api.html

## Using API key 
twitter = imp.load_source('twit', "C:/Users/ccara/Documents/School/Stats/Keys/twitter_key.py")
api = twitter.client

## See rate limit
limit = api.rate_limit_status()
limit.keys() ## look at dictionary's keys

wustl = api.get_user('WUSTL')
wustl 

wustl.followers_count

wustl_200 = api.followers(wustl.id, count = 200) ## up to 200
wustlfollowers1 = [f.screen_name for f in wustl_200]

wustlfollowersall = wustl.followers_ids()



##-------------------------------
yordan = api.get_user('cyordan')
yordan.followers_count


hisfollowers = []
for item in tweepy.Cursor(api.followers_ids, 'cyordan').items():
	hisfollowers.append(item)

len(hisfollowers)
hisfollowers    

i for i in hisfollowers:
    i.followers_count
    
i for i in hisfollowers:
    i.statuses_count 
    
hisfriends = []
for item in tweepy.Cursor(api.friends_ids, 'cyordan').items():
	hisfriends.append(item)

len(hisfriends)
hisfriends    
 
i for i in hisfriends:
    i.followers_count
    
i for i in hisfriends:
    i.statuses_count 

  