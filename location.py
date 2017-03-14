import api_keys as keys
import requests
import googlemaps

GEOCODING_URI = "https://www.googleapis.com/geolocation/v1/geolocate"
GECODING_KEY = keys.get_APIKey_for_Geolocation()
GMAPS_KEY = keys.get_APIKey_for_Geocoding()

# Get current lat and long based on location
def current_lat_long():
	payload = {"key": GECODING_KEY}
	location = requests.post(GEOCODING_URI, params=payload).json()
	return location["location"]

# Get lat and long for an inputted address
def lat_long_for_address(address):
	location = get_coordinates_for_decode(decode_location(address))
	return location

def decode_location(address):
	gmaps = googlemaps.Client(key = GMAPS_KEY)
	decode_result = gmaps.geocode(address)
	return decode_result

def get_coordinates_for_decode(decode_result):
	return decode_result[0]["geometry"]["location"]

