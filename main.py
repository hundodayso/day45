from bs4 import BeautifulSoup
import requests


url = "https://appbrewery.github.io/Zillow-Clone/"

webpage = requests.get(url).text
soup = BeautifulSoup(webpage, "html.parser")


cards = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")

links = [link.get("href") for link in cards]
print(links)
#for card in cards:

prices = soup.find(class_="PropertyCardWrapper__StyledPriceLine")
print(prices.get_text())

