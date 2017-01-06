from greengraph.greengraph import GreenGraph
from greengraph.googlemap import GoogleMap
from nose.tools import assert_equal, assert_almost_equal, assert_true, assert_raises
from unittest.mock import MagicMock, patch
import numpy as np

def test_input_correct():
	""" Check incorrect input do fail """
	with assert_raises(NameError) as exception:
		GreenGraph('a', 'cchicago')

	with assert_raises(TypeError) as exception:
		GreenGraph('a', 'b').green_between(5.2)

	with assert_raises(ValueError) as exception:
		GreenGraph('a', 'b').green_between(-20)
	
def test_geocode_lat_long_limit():
	""" Check lat and long are within limit """
	mydata = MagicMock()
	mydata.geolocate.side_effect = [GreenGraph.geolocate(city) for city in ['new york', 'chicago', 'london', 'sydney']]

	assert_true(mydata.geolocate()[0] < 90 and mydata.geolocate()[0] > -90)

	assert_true(mydata.geolocate()[1] < 180 and mydata.geolocate()[1] > -180)

def test_location_sequence_result():
	""" Check the new array to be of correct result """
	start = (50.0, 10.5)
	end = (60.0, 0.5)
	steps = 5
	my_array = GreenGraph.location_sequence(start, end, steps = steps)
	
	assert_true(my_array.shape == (steps, 2))

	assert_true(my_array.all() == np.array([[50.,10.5],[52.5,8.],[55.,5.5],[57.5,3.],[60.,0.5]]).all())

def test_green_input():
	""" Check the pixels input for green to be of shape (n,n,3) """
	
	with assert_raises(IndexError) as exception:
		c = np.array([[[1], [2]], [[3], [4]]])
		GoogleMap.green(c)
	
	with assert_raises(IndexError) as exception:
		c = np.array([[0, 1, 2], [3, 4, 5]])
		GoogleMap.green(c)

	with assert_raises(IndexError) as exception:
		c = np.array([[[1,3,2], [2,1,3]], [[1,3,3], [2,1,4]], [[3,2,4], [4,5,3]]])
		GoogleMap.green(c)

def test_count_green_result():
	""" Check count_green result to be correct """
	assert_true(GoogleMap(51.0, 0.0).count_green() == 156063)


def test_build_googleapi_params():
    # Check correct params are used
    import requests

    with patch.object(requests,'get') as mock_get:
    	mock_get.return_value = mock_response = MagicMock()
    	mock_response.content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x82'
    	default_map = GoogleMap(51.0, 0.4)

    	mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
            'sensor':'false',
            'zoom':12,
            'size':'400x400',
            'center':'51.0,0.4',
            'style':'feature:all|element:labels|visibility:off'
        		}
    		)

def test_overall_result():
	""" Check overall result to be correct """
	assert_true(GreenGraph('new york', 'chicago').green_between(5) == [60300, 157866, 152383, 150990, 28125])