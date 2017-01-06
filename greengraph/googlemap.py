import numpy as np
import geopy
from io import BytesIO
from matplotlib import image as img
import requests

class GoogleMap(object):
	"""Class that stores a PNG image then calculates the amount of green"""
	def __init__(self, lat, long, satellite=True,
					zoom=10, size=(400,400), sensor=False):
		"""Define the map parameters"""
		base="http://maps.googleapis.com/maps/api/staticmap?"
		params=dict(
				sensor= str(sensor).lower(),
				zoom= zoom,
				size= "x".join(map(str, size)),
				center= ",".join(map(str, (lat, long) )),
				style="feature:all|element:labels|visibility:off"
				)

		if satellite:
			params["maptype"]="satellite"

		# Fetch our PNG image data
		self.image = requests.get(base, params=params).content
		
		# Parse our PNG image as a numpy array
		self.pixels = img.imread(BytesIO(self.image))
	
	@staticmethod
	def green(pixels, threshold = 1.1):
		""" Use NumPy to build an element-by-element logical array """

		pixels = np.array(pixels)

		if (pixels.shape[2] != 3) or (pixels.shape[0] != pixels.shape[1]) or (len(pixels.shape) != 3):
			raise IndexError('The array must be of shape (n,n,3)')

		greener_than_red = pixels[:,:,1] > threshold * pixels[:,:,0]
		greener_than_blue = pixels[:,:,1] > threshold * pixels[:,:,2]
		green = np.logical_and(greener_than_red, greener_than_blue)
		return green

	def count_green(self, threshold = 1.1):
		return np.sum(self.green(self.pixels, threshold))

	def show_green(self, threshold = 1.1):
		green = self.green(threshold)
		out = green[:,:,np.newaxis] * np.array([0,1,0])[np.newaxis,np.newaxis,:]
		buffer = BytesIO()
		result = img.imsave(buffer, out, format='png')
		return buffer.getvalue()


