import requests as req
from datetime import datetime
from geopy.geocoders import Nominatim
import json


city_name = input("Please Enter City Name:")

geo_locator = Nominatim(user_agent="EB_weather_getter")
location = geo_locator.geocode(city_name)
latitude = location.latitude
longitude = location.longitude

url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'

response = req.get(url)

curent_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
file_name = city_name + '_' + curent_date + '.txt'
file = open(file_name,"w")
file.write(json.dumps(response.json(),indent=4))
file.close()

