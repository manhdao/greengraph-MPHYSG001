from greengraph.greengraph import GreenGraph
from greengraph.googlemap import GoogleMap
from nose.tools import assert_equal, assert_almost_equal, assert_true, assert_raises
from unittest.mock import MagicMock, patch

def test_input_correct():
	""" Check incorrect input do fail """
	with assert_raises(NameError) as exception:
		GreenGraph('a','b').geolocate('cchicago')

	with assert_raises(TypeError) as exception:
		GreenGraph('a','b').green_between(5.2)

	with assert_raises(ValueError) as exception:
		GreenGraph('a','b').green_between(-20)
	
def test_geocode_lat_long_limit():
	""" Check lat and long are within limit """
	mydata = MagicMock()
	mydata.geolocate.side_effect = [[52.43, -12.65],[57.43, 2.4],[24.65, -23.45],[51.00, 0.34]]

	assert_true(mydata.geolocate()[0] < 90 and mydata.geolocate()[0] > -90)

	assert_true(mydata.geolocate()[1] < 180 and mydata.geolocate()[1] > -180)

def test_location_sequence_result():
	""" Check the new array to be of correct result """
	import numpy as np

	start = (50.0, 10.5)
	end = (60.0, 0.5)
	steps = 5
	my_array = GreenGraph.location_sequence(start, end, steps = steps)
	
	assert_true(my_array.shape == (steps, 2))

	assert_true(my_array.all() == np.array([[50.,10.5],[52.5,8.],[55.,5.5],[57.5,3.],[60.,0.5]]).all())

# def 

"""def test_build_googleapi_params():
    # Check correct params are used
    import requests

    with patch.object(requests,'get') as mock_get:
    	default_map = GoogleMap(51.0, 0.0)

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
"""