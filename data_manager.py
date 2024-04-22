import requests
class DataManager:
    def __init__(self):
        self.view_url = "https://api.sheety.co/bb882804d345c5573d8f3b714bb1067e/flightDeals/prices"
        self.edit_url = "https://api.sheety.co/bb882804d345c5573d8f3b714bb1067e/flightDeals/prices/"
        self.users_url = "https://api.sheety.co/bb882804d345c5573d8f3b714bb1067e/flightDeals/names"
    def get_sheet_data(self):
        return requests.get(url=self.view_url)

    def get_user_emails(self):
        return requests.get(url=self.users_url)

    def add_iata_codes(self, text, row):
        params = {
            "price": {
                "iataCode": text
            }
        }
        requests.put(url=f"{self.edit_url}{row}", json=params)

    def add_lowest_price(self, text, row, column):
        params = {
            "price": {
                column: text
            }
        }
        requests.put(url=f"{self.edit_url}{row}", json=params)