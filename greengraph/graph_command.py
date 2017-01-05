from greengraph.greengraph import GreenGraph
from greengraph.googlemap import GoogleMap
from argparse import ArgumentParser

parser = ArgumentParser(description = "Generate pictures between 2 location")
parser.add_argument("-f", "--from", help="Starting location", dest='start')
parser.add_argument("-t", "--to", help="Ending location", dest='end')
parser.add_argument("-s", "--steps", help="Number of steps", type=int, dest='steps', default=20)
parser.add_argument("-o", "--out", help="Output filename", type=str, dest='filename', default=default_filename())