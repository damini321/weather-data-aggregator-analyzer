import requests
import json
from database import insert_data
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('API_KEY')

CITY = 'Aurangabad'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

def fetch_weather_data():
    response = requests.get(URL)
    data = response.json()
    return {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'timestamp': data['dt']
    }

# if __name__ == "__main__":
#     weather_data = fetch_weather_data()
#     print(weather_data)
if __name__ == "__main__":
    weather_data = fetch_weather_data()
    insert_data(weather_data)
    print(weather_data)