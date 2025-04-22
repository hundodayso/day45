from bs4 import BeautifulSoup
import requests
import smtplib
import keys


SENSOR_ID = "E21511"

environment_ep = "https://environment.data.gov.uk/flood-monitoring/id/measures"

params = {
    "stationReference": SENSOR_ID
}


response = requests.get(environment_ep, params=params)

webpage = response.json()
print(webpage)
#
# soup = BeautifulSoup(webpage, 'html.parser')
#
# #price = soup.select("div div span")
# price = soup.find(class_="a-offscreen").getText()
# price_without_currency = float(price.split("£")[1])
#
#
# print(price)
#
# print(price_without_currency)
#
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