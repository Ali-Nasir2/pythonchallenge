import json
import requests
from typing import Final

from model import Weather, dt

# Constants
API_key: Final[str] = 'YOUR_API_KEY_HERE' #get your api key from 'https://home.openweathermap.org/api_keys
Url: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather(city_name: str) -> dict:
    loading: dict = {'q': city_name, 'appid': API_key, 'units': 'metric'}
    
    response = requests.get(Url, params=loading)
    info: dict= response.json()
    return info

def get_wea_dtls(weather: dict) -> list[Weather]:

    days: list[dict] = weather.get('list')

    if not days:
        raise Exception(f'This can not continue cause of a problem in the backend: {weather}')

    # Try to add the info we want to our list_of_weather
    weather_list: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             descrip=weather[0].get('description'))
        weather_list.append(w)

    return weather_list
