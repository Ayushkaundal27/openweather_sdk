import requests
from sdk.openweather.common.enums.enum import Route

class ApiCall:
    def __init__(self, route, operation,auth):
        self.base_url = "https://api.openweathermap.org/data/2.5/"
        self.route = route
        self.operation = operation
        self.auth = auth

    def api_call(self):
        return requests.get(self.base_url+Route[self.route].value+self.operation,self.auth)

    
