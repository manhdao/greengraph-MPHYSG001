import numpy as np
import geopy

from googlemap import GoogleMap

class GreenGraph(object):
	def __init__(self, start, end):
		"""Initialise greengraph with 'start' and 'end' locations """
		if self.geolocate(start):
			self.start=start
		if self.geolocate(end):
			self.end=end	

	@staticmethod
	def geolocate(place):
		"""Return the geolocation of a given place"""
		n = geopy.geocoders.GoogleV3(domain="maps.google.co.uk").geocode(place, exactly_one=False)

		if n:
			return n[0][1]
		else:
			raise NameError("This place is not recognized by Google Map. Please check if the name is correct")

	@staticmethod
	def location_sequence(start, end, steps):
		"""Break distance between 'start' and 'end' into 'steps'"""
		if steps <= 0:
			raise ValueError("Number of steps must be positive")

		if type(steps) != int:
			raise TypeError("Number of steps must be integer")

		lats = np.linspace(start[0], end[0], steps)
		longs = np.linspace(start[1],end[1], steps)
		return np.vstack([lats, longs]).transpose()

	def green_between(self, steps):
		"""Return the amount of green in each of 'steps'"""
		return [GoogleMap(*location).count_green()
					for location in self.location_sequence(
							self.geolocate(self.start),
							self.geolocate(self.end), steps)]

