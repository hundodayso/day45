from bs4 import BeautifulSoup
import requests
import smtplib
import keys
from datetime import datetime


SENSOR_ID = "E21511"

environment_ep = "https://environment.data.gov.uk/flood-monitoring/id/measures"

params = {
    "stationReference": SENSOR_ID
}

response = requests.get(environment_ep, params=params)

river_level_data = response.json()

river_level = river_level_data["items"][0]["latestReading"]["value"]
date_time = river_level_data["items"][0]["latestReading"]["dateTime"]

formatted_date = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')
date_of_reading = formatted_date.strftime('%d-%m-%Y')
time_of_reading = formatted_date.strftime('%H:%M')

print(f'{time_of_reading= },{date_of_reading= }')

# ###SEND EMAIL HERE###
#
# title = soup.find(id="productTitle").get_text().strip()
# print(title)
#
#
# if price_without_currency < 100:
#     my_email = keys.email_addy
#     connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()
#     connection.login(user=keys.email_addy, password=keys.email_app_pw)
#     connection.sendmail(from_addr=keys.email_addy,
#                         to_addrs=keys.to_email,
#                         msg=f"Subject:Amazon Price Drop!\n\nPrice is less than 100! Click here to buy! {url}".encode("utf-8"))
#     connection.close()