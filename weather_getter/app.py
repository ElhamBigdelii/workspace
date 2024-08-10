import requests as req
from datetime import datetime
from geopy.geocoders import Nominatim
import json
import sys
import re


city_name = input("Please Enter City Name:")

if re.fullmatch(r'^[a-zA-Z\s]+$',city_name) == None:
    print("The city name is invalid.")
    sys.exit()

geo_locator = Nominatim(user_agent="EB_weather_getter")
location = geo_locator.geocode(city_name)

if location:
    if hasattr(location,'latitude'):
        latitude = location.latitude
    else:
        latitude = ""
    
    if hasattr(location,'longitude'):
        longitude = location.longitude
    else:
        latitude = ""
else:
    print("The City Name isn't Valid.")
    sys.exit()

url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m'

try:
    response = req.get(url,timeout=1) #1 second
except req.exceptions.RequestException as e:
    print(f"Connection error: {e}")
    sys.exit()

if response.status_code != 200 or response.content == b"":
    print(f'The connection failed because of: {response.reason}')
    sys.exit()

curent_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
file_name = city_name + '_' + curent_date + '.txt'

with open(file_name,"w") as resultFile:
    resultFile.write(json.dumps(response.json(),indent=4))

# if response.json().get('current') is not None:
# if 'current' in response.json()
try:
    current_temp = response.json()['current']['temperature_2m']
    print(f"{city_name}'s current temp is: {current_temp}")
except KeyError:
    print(f"An Error occur during get response. Please try later. Error is {KeyError}")

