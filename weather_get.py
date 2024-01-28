"""
Function to get Temperature from determinated local
"""
import requests
import time
from itertools import islice
from db_connect import *

api_key = 'a666087d339b3c675db1c8b86f7003f2'

city = input('Enter city name: ')
limit = 1

url_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}'

response_city = requests.get(url_city)
city_data = response_city.json()

lat = city_data[0]['lat']
lon = city_data[0]['lon']

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    data_list = data['daily']
    dados = []
    limit = 5
    for i in islice(data_list, limit):
        data_unix = i['dt']
        data_unix = int(data_unix)
        local_time = time.localtime(data_unix)
        local_time = time.strftime("%Y-%m-%d", local_time)
    
        # Temperature is in Celsius
        temp = i['temp']['day']
        
        dados.append({
            "Local": (city),
            "Data": (local_time),
            "Temperature": (temp)
                 })
        
    save_to_db(dados)
        
else:
    print('Error fetching weather data')