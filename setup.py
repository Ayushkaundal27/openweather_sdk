from sdk.open_weather import OpenWeather


api_key = "8560bfec3d03f64cbcc8eae684aa37da"
c = OpenWeather(api_key).current_weather(0, 0, "metric", "delhi", "html")
f = OpenWeather(api_key).weather_forecast(0, 0, "metric", "delhi", "xml")
print(c, f)
