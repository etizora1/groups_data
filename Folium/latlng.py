#!/usr/bin/python

import geocoder
from geopy import geocoders

def geopy_latlng(location, username='etizora', country='UK'):
	"""
	This function uses the GeoPy API.
	----from geopy import geocoders----
	Input :this function takes in a string

	PARAMETERS:
        country :specify which country you want to focus on
        username :to access the API you are required to sign up to the GeoNames 
                 service on http://www.geonames.org/ website
        Return :an array of coordinates is returned
	"""
	gn = geocoders.GeoNames(country_bias=country, username=username)
	address = gn.geocode(location)
	return [address.latitude, address.longitude]


def google_latlng(location):
	g = geocoder.google(location)
	return g.latlng
