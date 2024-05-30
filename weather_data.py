import sys
import requests

if sys.platform=="Linux":
    import Adafruit_CharLCD as LCD
else:
    class MockLCD:
        def clear(self):
            print("LCD Cleared")
        def message(self, text):
            print(f"LCD Message: {text}")
    LCD = MockLCD                

def getting_weather_data(Api_key, city):
    url = "http://api.weatherapi.com/v1/current.json"
    parameters = {
        "key": Api_key,
        "q": city
    }
    weather_response = requests.get(url, params=parameters)

    if weather_response.status_code==200:
        return weather_response.json()
    else:
        return None 

def displaying_weather_information_on_LCD(weather_data):
    lcd = LCD()
    if weather_data:
        location = weather_data['location']['name']
        temperature = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        
        print(location, temperature, condition)

        lcd.clear()
        
        lcd.message(f"{location} {temperature}C {condition}")
    else:
        lcd.message("Error fetching\nweather data")

Api_key = "5e409395fa6f485ebcc135413242905"
city = "Hyderabad"
weather_data = getting_weather_data(Api_key, city)
print(weather_data)
displaying_weather_information_on_LCD(weather_data)