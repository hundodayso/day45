from bs4 import BeautifulSoup
import requests
import re


url = "https://appbrewery.github.io/Zillow-Clone/"

webpage = requests.get(url).text
soup = BeautifulSoup(webpage, "html.parser")


cards = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")

links = [link.get("href") for link in cards]
print(links)
#for card in cards:


card_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices_as_int = [int("".join(re.findall(r'\d+', property.get_text()))) for property in card_prices]
prices_as_string = [re.sub(r"[+ /mo]", "", property.get_text()) for property in card_prices]
print(prices_as_int)
print(prices_as_string)
