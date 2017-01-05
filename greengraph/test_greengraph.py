from greengraph.greengraph import GreenGraph
from greengraph.googlemap import GoogleMap
from nose.tools import assert_equal, assert_almost_equal, assert_true, assert_raises
from unittest.mock import MagicMock, patch

def test_input_correct():
	""" Check incorrect input do fail """
	
	with assert_raises(NameError) as exception:
		GreenGraph('new york','cchicago')

	with assert_raises(TypeError) as exception:
		GreenGraph('new york', 'chicago').green_between(5.2)

	with assert_raises(ValueError) as exception:
		GreenGraph('new york', 'chicago').green_between(-20)

"""def test_geocode_lat_long_limit():

	start = MagicMock()
	end = MagicMock()
	place = MagicMock()

	mydata = GreenGraph(start, end)

	assert_true(mydata.geolocate(place)[0] < 90 and mydata.geolocate(place)[0] > -90)

	assert_true(mydata.geolocate(place)[1] < 180 and mydata.geolocate(place)[1] > -180)
"""

def test_build_googleapi_params():
    """ Check correct params are used """
    import requests

    with patch.object(requests,'get') as mock_get:
        default_map = GoogleMap(51.0, 0.0).pixels

        mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
            'sensor':'false',
            'zoom':12,
            'size':'400x400',
            'center':'51.0,0.0',
            'style':'feature:all|element:labels|visibility:off'
        		}
    		)