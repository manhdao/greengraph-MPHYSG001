from greengraph.greengraph import GreenGraph
from greengraph.googlemap import GoogleMap
from nose.tools import assert_equal, assert_almost_equal, assert_true, assert_raises
from mock import MagicMock

def test_input_correct():
	""" Check incorrect input do fail """

	with assert_raises(ValueError) as exception:
		GreenGraph('New York','Cchicago')


	#with assert_raises()