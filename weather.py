import googlemaps
import api_keys as keys
import requests

gmaps_key = keys.get_APIKey_for_geocoding()
weather_key = keys.get_APIKey_for_DarkSkyWeather()

def decode_location(address):
	gmaps = googlemaps.Client(key = gmaps_key)
	decode_result = gmaps.geocode(address)
	return decode_result

def get_coordinates_for_decode(decode_result):
	return decode_result[0]["geometry"]["location"]

def get_weather_for_coordinates(coordinates):
	# URL/Key/Lat,Long
	base_url = "https://api.darksky.net/forecast/"
	request_url = base_url + weather_key + "/" + str(coordinates["lat"]) + "," + str(coordinates["long"])
	results = requests.get(request_url)

def get_weather_for_address(address):
	coordinates = get_coordinates_for_decode(decode_location(address))
	# URL/Key/Lat,Long
	base_url = "https://api.darksky.net/forecast/"
	request_url = base_url + weather_key + "/" + str(coordinates["lat"]) + "," + str(coordinates["lng"])
	payload = {"exclude": ["minutely,hourly,daily,alerts,flags"]}
	results = requests.get(request_url, params = payload).json()
	temperatures = {"Temp": results["currently"]["temperature"], "apparentTemp": results["currently"]["apparentTemperature"]}
	print(temperatures)

get_weather_for_address("8102 W Oklahoma Ave, West Allis, WI 53219")








