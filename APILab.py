import requests
import os

def main():
    city = input('Enter a city: ')
    cn = input('Enter a country: ')
    try:
        key = os.environ.get('WEATHER_KEY')
        query = {'q': f'{city},{cn}', 'units':'imperial', 'appid': key}

        url = 'https://api.openweathermap.org/data/2.5/forecast'

        data = requests.get(url, params=query).json()
        weather_description = data["list"][0]["weather"][0]["description"]
        temp_f = data['list'][0]['main']['temp']
        wind_speed = data['list'][0]['wind']['speed']
        print(f'The weather is {weather_description}, the temperature is {temp_f:.2f}F with a wind speed of {wind_speed}mph.')
    except TypeError as e:
        print(e)
    except KeyError:
        print(data['message'])

if __name__=='__main__':
    main()