import numpy as np
import geopy

from greengraph.googlemap import GoogleMap as GMap

class Greengraph(object):
	def __init__(self, start, end):
		"""Initialise greengraph with 'start' and 'end' locations """
		self.start=start
		self.end=end
		self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

	def geolocate(self, place):
		"""Return the geolocation of a given place"""
		return self.geocoder.geocode(place,exactly_one=False)[0][1]

	def location_sequence(self, start,end,steps):
		"""Break distance between 'start' and 'end' into 'steps'"""
		lats = np.linspace(start[0], end[0], steps)
		longs = np.linspace(start[1],end[1], steps)
		return np.vstack([lats, longs]).transpose()

	def green_between(self, steps):
		"""Return the amount of green in each of 'steps'"""
		return [GMap(*location).count_green()
					for location in self.location_sequence(
							self.geolocate(self.start),
							self.geolocate(self.end), steps)]

