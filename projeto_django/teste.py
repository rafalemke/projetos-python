import requests
ip = '170.244.78.204'
def get_location(ip):
    YOUR_ACCESS_KEY = '4b25b7d068d90fd4511ec360d0ae67c4'
    response = requests.get(f'http://api.ipstack.com/{ip}?access_key={YOUR_ACCESS_KEY}')
    geodata = response.json()
    return geodata['city']

# print(get_location(ip))



def get_weather_data(cidade):
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=dd8102c525204cbb900230149243103&q={cidade}')
    weather_data = response.json()
    return weather_data['current']


clima = get_weather_data(get_location(ip))

print(clima)