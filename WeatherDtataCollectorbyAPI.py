#Simple Project by Statue_Of_Bashar
#More City IDs are found in city.list.json file
import requests
import json
import datetime

print ("City ID : \nSylhet = 1185099\nDhaka = 1185241\nGazipur = 1185098\nKishorgonj = 1337249")
u = input("Enter City ID : ")
if u == "":
    u = "1185099"

URL = "https://api.openweathermap.org/data/2.5/weather?id="+u+"&units=metric&appid=54e9a5a7f29b36069e7e1f9c162d1b26"
payload = {"id": u, "APPID": "54e9a5a7f29b36069e7e1f9c162d1b26"}

r = requests.get(URL, params = payload)

result = r.json()
#print(json.dumps(result, indent = 4))

print("Current Weather of " + result['sys']['country'] + "-" + result['name']+  ":")
print("Time Zone : GMT", result['timezone']/3600)
print("Weather Condition : ", result["weather"][0]["description"])
print("Temperature : " , result["main"]["temp"] , "\nBut feels like :" , result['main']['feels_like'])
print("Air Pressure : ", result['main']['pressure']/1013.2501, "atm")
print("Humidity : ", result["main"]["humidity"], "%")
print("Wind Speed : ", result['wind']["speed"]*3.6, "km/h")
print("SunRise : ", datetime.datetime.fromtimestamp(result['sys']['sunrise']).strftime("%d-%b-%Y %I:%M:%S %p"))
print("SunSet : ", datetime.datetime.fromtimestamp(result['sys']['sunset']).strftime("%d-%b-%Y %I:%M:%S %p"))