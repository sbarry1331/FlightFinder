import requests
from datetime import datetime

class FlightSearch:

    def __init__(self):
        self.API_KEY = "DPjdHA2NFXRZ9UrhN4alaRimO27Cludm"
        self.code_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.flight_endpoint = "https://api.tequila.kiwi.com/v2/search"

    def retrieve_codes(self, city):
        header = {
            "apikey": self.API_KEY
        }
        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=self.code_endpoint, params=params, headers=header)
        return response.json()["locations"][0]["code"]

    def find_flights(self, to_city, from_city):
        today = datetime.now()
        rn = today.strftime('%d/%m/%Y')
        six_months = int(today.strftime('%m'))
        six_months += 6
        six_months %= 12
        header = {
            "apikey": self.API_KEY
        }
        params = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": rn,
            "date_to": today.strftime(f'%d/{six_months}/%Y'),
            "curr": "USD",
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 14,
        }
        response = requests.get(url=self.flight_endpoint, params=params, headers=header)
        return response.json()
