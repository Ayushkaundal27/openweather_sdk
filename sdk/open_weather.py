from sdk.openweather.current_weather_function.current_weather import CurrentWeather 
from sdk.openweather.forecast.forecast import WeatherForecast


class OpenWeather:
    def __init__(self, api_key):
        self.api_key = api_key

    def current_weather(self, lat:str = 0, log:str = 0, unit:str = None, lang:str = None, city:str = None, mode_of_response:str = None):
        return CurrentWeather(lat, log, self.api_key, unit, lang,city, mode_of_response).current_weather().text
     
    def weather_forecast(self, lat:str = 0, log:str = 0, unit:str = None, lang:str = None, city:str = None, mode_of_response:str = None):
        return WeatherForecast(lat, log, self.api_key, unit, lang,city, mode_of_response).weather_forecast().text