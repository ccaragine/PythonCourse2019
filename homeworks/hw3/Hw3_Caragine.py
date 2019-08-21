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

## getting all followers of WUSTL
hisfollowers = []
for item in tweepy.Cursor(api.followers_ids, 'WUSTL').items(10):
	hisfollowers.append(item)

############## Question 1 ##############
## getting all statuses of WUSTL's followers
hisfollowersstatus = []
for i in hisfollowers:
    hisfollowersstatus.append(api.get_user(i).statuses_count)

hisfollowersstatus.sort(reverse=True)  
api.get_user(hisfollowersstatus[0])

############## Question 2 #################
## getting all followers of WUSTL's followers
hisfollowerscount = []
for i in hisfollowers:
    hisfollowerscount.append(api.get_user(i).followers_count)

hisfollowerscount.sort(reverse=True)
api.get_user(hisfollowerscount[0])

 

############ Question 3 ##################
## among those he follows, who has the most followers
hisfriends = []
for item in tweepy.Cursor(api.friends_ids, 'WUSTL').items(10):
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

pscfollowers2 = []
for i in pscfollowers:
  try:
      for j in tweepy.Cursor(api.followers_ids, i ).items(10):
          pscfollowers2.append(j)
  except: 
      continue 
  
pscfollowers2status = []
for i in pscfollowers2:
    pscfollowers2status.append(api.get_user(i).statuses_count)

pscfollowers2.sort(reverse=True)    
pscfollowers2[0]  
 
################## Question 6 ######################
## Friends of Wustl's friends, who has the most tweets 
pscfriends = []
for item in tweepy.Cursor(api.friends_ids, 'WUSTLPoliSci').items(10):
	pscfriends.append(item)

pscfriends2 = []
for i in pscfriends2:
  try:
      for j in tweepy.Cursor(api.friends_ids, i ).items(10):
          pscfriends2.append(j)
  except: 
      continue 
  
pscfriends2status = []
for i in pscfriends2:
    pscfriends2status.append(api.get_user(i).statuses_count)

pscfriends2status.sort(reverse=True)    
pscfriends2status[0]  


    











  