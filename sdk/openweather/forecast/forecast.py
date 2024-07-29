from sdk.openweather.common.api_calls_handler.api_call import ApiCall


class WeatherForecast:
    def __init__(self, lat, log, api_key, unit=None, lang=None, city_or_pincode=None,mode=None):
        self.lat = lat
        self.log = log
        self.api_key=api_key
        self.unit=unit
        self.lang=lang
        self.city_or_pincode = city_or_pincode
        self.mode = mode

    def weather_forecast(self):
        operation = ""
        if self.city_or_pincode is not None:
            operation = f"q={self.city_or_pincode}"
        else:
            operation = f"lat={self.lat}&lon={self.log}"
        if self.unit is not None:
            temp = f"&units={self.unit}"
            operation = operation + temp
        if self.lang is not None:
            temp = f"&lang={self.lang}"
            operation = operation + temp 
        if self.mode is not None:
            temp = f"&mode={self.mode}"
            operation = operation + temp       
                      
        api_response = ApiCall('weather',operation,f"&appid={self.api_key}").api_call()

        return api_response
