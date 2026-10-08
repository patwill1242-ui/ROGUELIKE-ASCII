#istall requests 
#request allow sent HTTP request easily,and return the info in format JSON

import json,requests

API_KEY = "your API"
CITY = "Milan"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=en"

def weather_forecast():
    try:
        answer = requests.get(url)
        weather_data = answer.json()

        if answer.status_code == 200:   #the client request was successfully received, understood, and processed by the server
            
            # print(json.dumps(weather_data, indent=4))   see the json answer

            temperature = weather_data["main"]["temp"]
            thermal_sensation = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]

            print("The weather today in Milan")
            print(f"Temperature : {temperature}, thermal_sensation : {thermal_sensation}")
            print(f"Humidity : {humidity}")
            print(f"State : {description.capitalize()}")

        else:
            print("ERRORE revise your API please")
    except Exception as e:
        print(f"ERROR CONNECTION : {e}")

if __name__ == "__main__":
    weather_forecast()


