############## Homework 3 ##############
## Crystal Caragine
## 8/16/2019
## Hw3_Caragine

## Importing packages 
import tweepy
# http://docs.tweepy.org/en/v3.8.0/api.html

import imp
import sys

sys.path.insert(0, '"C:/Users/ccara/Documents/School/Stats/Keys/')

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
yordan.statuses_count

## getting all followers of Yordan
hisfollowers = []
for item in tweepy.Cursor(api.followers_ids, 'cyordan').items(10):
	hisfollowers.append(item)

############## Question 1 ##############
## getting all statuses of Yordan's followers
hisfollowersstatus = []
for i in hisfollowers:
    hisfollowersstatus.append(api.get_user(i).statuses_count)

hisfollowersstatus.sort(reverse=True)  
api.get_user(hisfollowersstatus[0])

############## Question 2 #################
## getting all followers of Yordan's followers
hisfollowerscount = []
for i in hisfollowers:
    hisfollowerscount.append(api.get_user(i).followers_count)

hisfollowerscount.sort(reverse=True)
api.get_user(hisfollowerscount[0])

## If time extract name 

############ Question 3 ##################
## among those he follows, who has the most followers
hisfriends = []
for item in tweepy.Cursor(api.friends_ids, 'cyordan').items(10):
	hisfriends.append(item)

hisfriendsfollowers = []
for i in hisfriends:
    hisfriendsfollowers.append(api.get_user(i).followers_count)

hisfriendsfollowers.sort(reverse=True)
api.get_user(hisfriendsfollowers[0])



############ Question 4 ##################
## Among those he follows, who has the most tweets

hisfriendsstatus = []
for i in hisfriends:
    hisfriendsstatus.append(api.get_user(i).statuses_count)

hisfriendsstatus.sort(reverse=True)
api.get_user(hisfriendsstatus[0])


############ Question 5 #####################
wustlpsci = api.get_user('WUSTLPoliSci')
wustlpsci.followers_count

## the IDs of Followers of political science
pscfollowers = []
for item in tweepy.Cursor(api.followers_ids, 'WUSTLPoliSci').items(10):
	pscfollowers.append(item)

## Among the followers of political science, how many followers they have  
pscfollowerscount = []
for i in pscfollowers:
    pscfollowerscount.append(api.get_user(i).followers_count)

pscfollowerstwo = []
for item in tweepy.Cursor(api.followers_ids, pscfollowerscount).items(10):
	pscfollowers.append(item)








  