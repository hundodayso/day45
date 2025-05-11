from bs4 import BeautifulSoup
import requests


url = "https://appbrewery.github.io/Zillow-Clone/"

webpage = requests.get(url).text
soup = BeautifulSoup(webpage, "html.parser")

print(soup)