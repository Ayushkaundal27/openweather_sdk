from sdk.open_weather import OpenWeather 


c=OpenWeather("8560bfec3d03f64cbcc8eae684aa37da").current_weather(0,0,unit="metric",city="delhi",mode_of_response="html")
f=OpenWeather("8560bfec3d03f64cbcc8eae684aa37da").weather_forecast(0,0,unit="metric",city="delhi",mode_of_response="xml")
print(c,f)