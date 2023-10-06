'''
You need to install requests
pip install reqests
pip3 install reqests
python -m pip install reqests
python3 -m pip install reqests
'''
import requests

# fetch weather API key from https://home.openweathermap.org
API_KEY = 'cb75949cfaffb088b942355d27e779fd'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = 'Seoul'
# city = input('Enter a city name: ')

request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

'''
sample result of data. json. Note! it is dictionary:
{'coord': {'lon': 151.2073, 'lat': -33.8679}, 
'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 
'base': 'stations', 
'main': {'temp': 293.11, 'feels_like': 293.12, 'temp_min': 291.76, 'temp_max': 295.8, 'pressure': 1022, 'humidity': 75}, 
'visibility': 10000, 
'wind': {'speed': 9.77, 'deg': 180}, 
'clouds': {'all': 40}, 
'dt': 1695685540, 
'sys': {'type': 2, 'id': 2018875, 'country': 'AU', 'sunrise': 1695670813, 'sunset': 1695714801}, 
'timezone': 36000, 'id': 2147714, 'name': 'Sydney', 'cod': 200}
'''

# check the status code if the request is successful
if response.status_code == 200:
    data = response.json()
    weather = data['weather']    
    temperature = data['main']['temp'] 
    # the default value is in kelvin. converting to Celsius, and round to interger
    temperature = round(temperature - 273.15)
    description = data['weather'][0]['description']   

    print('Weather is', weather)
    print('Temperature is', temperature) # the value is in Kelvin. WTF! You need to convert to C.
    print('Description is', description)

else:
    print('An error occurred')






