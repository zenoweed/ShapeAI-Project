#Name = Brian Fernandes
#emailID = nestanwork@gmail.com

import requests
#import os
from datetime import datetime

api_key = '543d202fbbe7a00eca772fb1f8effb75'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store & display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

info = open('Temperaturedata.txt','w')
# Create a text file if it doesn't exist or writes into the text file if it exist.

info.write("-------------------------------------------------------------\n")
info.write ("Weather Status at {}  on {}\n".format(location.upper(), date_time))
# for writing weather status of a particular place at particular time and date in to text file.
info.write ("-------------------------------------------------------------\n")

info.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
# for writing current temperature in to text file.
info.write("Current weather desc  : {}\n".format(weather_desc))
# for writing current Weather in to text file.
info.write("Current Humidity      : {} %\n".format(hmdt))
# for writing current percentage of Humidity in to text file.
info.write("Current wind speed    : {} KMPH".format(wind_spd))
# for writing current wind speed in to text file.
info.close()
# for closing the text file which has been opened.