import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def get_weather(city):
    result = requests.get(url.format(city,'99c9db04fb83ce087fb75dedc820a6ae'))
    print(result.content)
    if result:
        json = result.json() 
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_farenheit = (temp_celsius) * 9/5 +32
        weather = json['weather'][0]['main']
        a=str(temp_celsius)
        temp_celsius=a[0:4]
        final = (city,country,temp_celsius,temp_farenheit,weather)
        print(final) 

    else:
        return None

get_weather('Mumbai') 