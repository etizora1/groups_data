#!/usr/bin/python

import geocoder
import numpy as np
from geopy import geocoders
from geopy.geocoders import Nominatim

def geopy_latlng(location, username='et1234', country='UK'):
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
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(location + ", UK", timeout=120)
    except AttributeError:
        print('%s' %(location) + '--failed--')
    return [location.latitude, location.longitude]


def google_latlng_2(location):
	g = geocoder.google(location + ", UK")
	return g.latlng


def latlng_finder(data, file_name, method=google_latlng):
    """
    :param: data -some type of array containing list of place name you want ot query
    :param: file_name -this function saves the array of coordinates
    :param: method -choose the function you would like to use to find the latitude
            longitude
    """

    coordinates = []
    for x in data:
        try:
            coordinates.append(method(x))
        except AttributeError:
            coordinates.append('Nan')
        else:
            time.sleep(2)
            coordinates.append(method(x))
        print(x)
    
    np.save(('%s'% (file_name)) + '.npy', coordinates)
    
    return coordinates