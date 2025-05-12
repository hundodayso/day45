from bs4 import BeautifulSoup
import requests


url = "https://appbrewery.github.io/Zillow-Clone/"

webpage = requests.get(url).text
soup = BeautifulSoup(webpage, "html.parser")

cards = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
for card in cards:

    print(card.get("href"))