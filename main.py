from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification = NotificationManager()
excel = DataManager()
flight_search = FlightSearch()
response = excel.get_sheet_data()
datasheet = response.json()
number = 2
flight_prices = []

for row in datasheet["prices"]:
    aita_code = flight_search.retrieve_codes(row['city'])  # Call to find each city AITA Codes
    excel.add_iata_codes(aita_code, number)  # Add codes to GoogleSheet
    try:
        flights = flight_search.find_flights(aita_code, "PIT")["data"][0]  # Grab the single cheapest option in the returned flights JSON
    except IndexError:  # No flights found, so skip and go to next city
        continue
    excel.add_lowest_price(flights["price"], number, "cheapest")  # Add the cheapest flight price to google sheet
    flight_prices.append(flights["price"])
    if int(row['lowestPrice']) > flight_prices[row['id'] - 2]:
        message = f"Low price alert! Only ${flights['price']} to fly from {flights['cityFrom']}-{flights['cityCodeFrom']} to {flights['cityTo']}-{flights['cityCodeTo']}, from {flights["local_departure"].split("T")[0]} to {flights["route"][-1]["local_departure"].split("T")[0]}.\n\n{flights['deep_link']}"
        notification.send_mail(message)
    number += 1

number = 2
flight_prices = []
for row in datasheet["prices"]:
    aita_code = flight_search.retrieve_codes(row['city'])  # Call to find each city AITA Codes
    try:
        flights = flight_search.find_flights(aita_code, "IAD")["data"][0]  # Grab the single cheapest option in the returned flights JSON
    except IndexError:  # No flights found, so skip and go to next city
        continue
    excel.add_lowest_price(flights["price"], number, "chepest")  # Add the cheapest flight price to google sheet
    flight_prices.append(flights["price"])
    if int(row['lowestPrice']) > flight_prices[row['id'] - 2]:
        message = f"Low price alert! Only ${flights['price']} to fly from {flights['cityFrom']}-{flights['cityCodeFrom']} to {flights['cityTo']}-{flights['cityCodeTo']}, from {flights["local_departure"].split("T")[0]} to {flights["route"][-1]["local_departure"].split("T")[0]}.\n\n{flights['deep_link']}"
        notification.send_mail(message)
    number += 1

