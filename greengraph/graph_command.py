#!/usr/bin/env python
from .greengraph import GreenGraph
from .googlemap import GoogleMap
from argparse import ArgumentParser
from IPython.display import Image
from IPython.display import display

if __name__ == "__main__":

	parser = ArgumentParser(description = 'Generate pictures between 2 location')
	parser.add_argument('-f', '--from', required=True, help='Starting location', dest='start')
	parser.add_argument('-t', '--to', required=True, help='Ending location', dest='end')
	parser.add_argument('-s', '--steps', help='Number of steps', type=int, dest='steps', nargs='?', default=10)
	parser.add_argument('-gb', '--greenbetween', help='Count green between', dest='greenbetween', action="store_true")
	parser.add_argument('-o', '--out', help='Output filename', type=str, dest='filename')

	args = parser.parse_args()

	my_data = GreenGraph(args.start, args.end)

	if args.greenbetween:
		print(my_data.green_between(args.steps))

	if args.filename:
		imgs = (GoogleMap(*location) 
			for location in GreenGraph.location_sequence(GreenGraph.geolocate('london'),
                                                         GreenGraph.geolocate('oxford'), steps=args.steps))
		for position, img in enumerate(imgs):
			with open(args.filename+'_{0}.png'.format(position+1), 'wb') as png:
				png.write(img.image)
