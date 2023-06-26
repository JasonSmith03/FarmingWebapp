### Author Jason Smith

#import required modules
import requests
import json

#Constants
API_KEY = "9a2e73e398916e32cf89678863639dd4"
CITY_NAME = "MAPLE"
#Open Weather map API version 2.5
URL = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + CITY_NAME

def kelvinToCelsius(temperature):
    #conversion formula C = K – 273.15
    celsius = temperature - 273.15
    return str(round(celsius))

def getWeather(URL):
    openWeatherResponse = requests.get(URL)

    jsonResponse = openWeatherResponse.json()

    # Now jsonResponse contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if jsonResponse["cod"] != "404":
     
        # store the value of "main"
        # key in variable mainResp
        mainResp = jsonResponse["main"]
     
        # store the value corresponding
        # to the "temp" key of mainResp
        current_temperature = mainResp["temp"]
    
     
        # store the value corresponding
        # to the "humidity" key of mainResp
        current_humidity = mainResp["humidity"]
     
        # store the value of "weather"
        # key in variable weatherResp
        weatherResp = jsonResponse["weather"]
     
        # store the value corresponding
        # to the "description" key at
        # the 0th index of weatherResp
        weather_description = weatherResp[0]["description"]
        
     
        # print following values
        print(" Temperature = " +
                        kelvinToCelsius(current_temperature) + "°C"
              "\n humidity (in percentage) = " +
                        str(current_humidity) + "%"
              "\n description = " +
                        str(weather_description))
        return [kelvinToCelsius(current_temperature), str(current_humidity), str(weather_description)]
     
    else:
        print(" City Not Found ")

#Main function where code begins
def main():
    getWeather(URL)

if __name__ == "__main__":
    main()
