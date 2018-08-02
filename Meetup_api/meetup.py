#!/usr/bin/python

import urllib
import json
import time
import os
import os.path
import requests
import numpy as np
import pandas as pd

def meetups_api(places, topic, key, search_radius=100):
	""" A function to use the meetups API
    
	:places, list/array type object with geo coordinates min of 2 location
    
	:topic, type of group you're looking or e.g. running, sewing
    
	:key, API key from https://www.meetup.com/meetup_api/
    
	:search_radius, search radius in miles from centre point
    
	"""
    
	urls = []
	for place in places:
		urls.append('https://api.meetup.com/2/groups?key='+key+'&country=GB&city&lat='
                    +str(place[0])+'&lon='+str(place[1])+ '&radius='
                    +str(search_radius)+'&data_format=json&fields=id,name,description,members&topic='
                    +topic+ '&page=10000')
	print('----%d urls created----'%len(urls))

	urls = urls
	for url in urls:
		#counter += 1
		time.sleep(5)
		response = requests.get(url)
		data =response.json()
		data=data["results"] #accessed data of results key only
		if len(data)!= 0:
			new_npy = np.load('meetup_%s.npy'%topic) if os.path.isfile('meetup_%s.npy'%topic) else [] #get data if exist
			np.save('meetup_%s.npy'%topic,np.append(new_npy,data)) #save the new
		else:
			pass
		print(url)
    
	#saving the data on your current working dir
	#new_npy = np.load('meetup_%s.npy'%topic) if os.path.isfile('meetup_%s.npy'%topic) else [] #get data if exist
	#np.save('meetup_%s.npy'%topic,np.append(new_npy,data)) #save the new
	#with open('meetup_%s.npy'%topic, 'a') as d:
		#json.dump(data, d, indent=4)
    
# turning everything into a nice dataframe
def tidy_meetup(topic):
	message= "--(meetup_%s.npy) doesn't exist--"%topic
	data= 'meetup_%s.npy'%topic
	groups = np.load(data) if os.path.isfile(data) else print(message)
	city,country,lat,lon,name,members, = [],[],[],[],[],[]
	
	try:
		for grp in groups:
			city.append(grp['city'])
			country.append(grp['country'])
			lat.append([grp['lat']])
			lon.append([grp['lon']])
			name.append(grp['name'])
			members.append(grp['members'])
    
		df = pd.DataFrame([city,country,lat,lon,name,members]).T
		df.columns=['city','country','lat','lon','name','members']
    
		return df
	except TypeError:
		print('--please check/move file into current working directory--')


if __name__ == "__main__":
	meetups_api()
	tidy_meetup()
