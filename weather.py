import requests
import datetime


now = datetime.datetime.now()

api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=426767ea170627f14a06a5979bea2de4&q='

city = input('\nplease enter the city name: '.title())

unit = '&units=imperial'

url = api_address + city + unit

json_data = requests.get(url).json()
json_data2 = requests.get(url).json()
json_data3 = requests.get(url).json()
json_data4 = requests.get(url).json()
json_data5 = requests.get(url).json()
json_data6 = requests.get(url).json()
json_data7 = requests.get(url).json()
json_data8 = requests.get(url).json()


formatted_data = json_data['weather'][0]['main']
formatted_data2 = json_data2['weather'][0]['description']
formatted_data3 = json_data3['wind']['speed']
formatted_data4 = json_data4['main']['humidity']
formatted_data5 = json_data5['main']['temp']
formatted_data6 = json_data6['main']['temp_min']
formatted_data7 = json_data7['main']['temp_max']
formatted_data8 = json_data8['main']['feels_like']

print("\n----- Here are the current weather conditions for: {} -----".format(city).title())

print()
print('current and date time: '.title())
print(now.strftime('%Y-%m-%d %H:%M:%S'))

print()
print('Weather:\t {}\nDescription:\t {}\nWind speed:\t {}\nHumidity:\t {}'.format(formatted_data, formatted_data2, formatted_data3, formatted_data4).title())

print('temp:\t\t {}\nTemp min:\t {}\ntemp max:\t {}\nfeel like:\t {}'.format(formatted_data5, formatted_data6, formatted_data7, formatted_data8).title())

print()
