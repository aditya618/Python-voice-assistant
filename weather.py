import requests

# andhra pradesh id = 1278629

url = "http://api.openweathermap.org/data/2.5/weather?id=1278629&appid="+""

json_data = requests.get(url).json()
# print(json_data)
def temperature():
    temperature = round(json_data["main"]["temp"] - 273,1)
    return temperature

def desc():
    description = json_data['weather'][0]['description']
    return description
