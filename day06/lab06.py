# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 


import imp
import sys

sys.path.insert(0, '"C:/Users/ccara/Documents/School/Stats/Keys/')
imported_items = imp.load_source('google', "C:/Users/ccara/Documents/School/Stats/Keys/google_key.py")
gmaps = imported_items.client

## Finding the embassy that is closests 
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
whlocation = gmaps.geocode(whitehouse)
whlatlong = whlocation[0]['geometry']['location']


embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

embassy1loc = {'lat':38.917228, 'lng': -77.0522365}
embassy2loc = {'lat': 38.9076502, 'lng':-77.0370427}
embassy3loc = {'lat':38.916944 , 'lng':-77.048739}


embassy1 = gmaps.reverse_geocode({'lat': 38.917228, 'lng': -77.0522365 })
embassy2 = gmaps.reverse_geocode({'lat': 38.9076502, 'lng':-77.0370427  })
embassy3 = gmaps.reverse_geocode({'lat':38.916944 , 'lng':-77.048739})

distance = gmaps.distance_matrix(embassy1loc, whlatlong)
print(distance['rows'][0]['elements'][0]['distance']['text'])

distance2 = gmaps.distance_matrix(embassy2loc, whlatlong)
print(distance2['rows'][0]['elements'][0]['distance']['text'])

distance3 = gmaps.distance_matrix(embassy3loc, whlatlong)
print(distance3['rows'][0]['elements'][0]['distance']['text'])

## Embassy 2 is the closests to the Whitehouse

gmaps.places_nearby(embassy2loc, 15, type= "breakfast")
## Washington is the closests breakfast place 

gmaps.places_nearby(embassy2loc, 15, type= "resturant")


