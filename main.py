from bs4 import BeautifulSoup
import requests
import smtplib
import keys

url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url)

webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

#price = soup.select("div div span")
price = soup.find(class_="aok-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

my_email = keys.email_addy

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=keys.email_addy, password=keys.email_app_pw)
connection.sendmail(from_addr=keys.email_addy, to_addrs=keys.to_email, msg="hello")
connection.close()