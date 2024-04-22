import smtplib
from data_manager import DataManager

MY_EMAIL = "sbarry1331@gmail.com"
PASSWORD = "klposkvzuddhgvse"
GET_URL = "https://api.sheety.co/bb882804d345c5573d8f3b714bb1067e/flightDeals/names"
class NotificationManager:

    def send_mail(self, message):  # Send email given the name and email
        data = DataManager()
        response = data.get_user_emails().json()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for user in response['names']:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=user['email'], msg=f"Subject:Flight Deal!\n\n{message}")
