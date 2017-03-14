import api_keys as keys
import requests
import location

WEATHER_KEY = keys.get_APIKey_for_DarkSkyWeather()
BASE_URL = "https://api.darksky.net/forecast/"

def get_weather_for_address(address):
	coordinates = location.lat_long_for_address(address)
	# URL/Key/Lat,Long
	BASE_URL = "https://api.darksky.net/forecast/"
	request_url = BASE_URL + WEATHER_KEY + "/" + str(coordinates["lat"]) + "," + str(coordinates["lng"])
	payload = {"exclude": ["minutely,hourly,daily,alerts,flags"]}
	results = requests.get(request_url, params = payload).json()
	temperatures = {"Temp": results["currently"]["temperature"], "apparentTemp": results["currently"]["apparentTemperature"]}
	print(temperatures)

def get_weather_for_current_location():
	coordinates = location.current_lat_long()
	# URL/Key/Lat,Long
	BASE_URL = "https://api.darksky.net/forecast/"
	request_url = BASE_URL + WEATHER_KEY + "/" + str(coordinates["lat"]) + "," + str(coordinates["lng"])
	payload = {"exclude": ["minutely,hourly,daily,alerts,flags"]}
	results = requests.get(request_url, params = payload).json()
	temperatures = {"Temp": results["currently"]["temperature"], "apparentTemp": results["currently"]["apparentTemperature"]}
	print(temperatures)

get_weather_for_address("Zurich Mariott Hotel")
get_weather_for_current_location()








