from sdk.open_weather import OpenWeather 


p=OpenWeather("8560bfec3d03f64cbcc8eae684aa37da").current_weather(0,0,unit="metric",city="delhi",mode_of_response="html")
print(p)