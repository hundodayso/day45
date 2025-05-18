from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import keys

url = "https://appbrewery.github.io/Zillow-Clone/"

form_url = keys.form_url

webpage = requests.get(url).text
soup = BeautifulSoup(webpage, "html.parser")


cards = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")


links = [link.get("href") for link in cards]
print(links)
#for card in cards:


card_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
#prices_as_int = [int("".join(re.findall(r'\d+', property.get_text()))) for property in card_prices]
#prices_as_string = [re.sub(r"[+ /mo|\1bd]", "", property.get_text()) for property in card_prices]
prices_as_string = [re.split(r"\+|/", property.get_text())[0] for property in card_prices]
#print(prices_as_int)
print(prices_as_string)



card_addresses = soup.find_all(name="address")
addresses = [address.get_text().replace("|","").strip() for address in card_addresses]
#addresses2 = [re.sub(r"[|]".strip(),"", address.get_text()) for address in card_addresses]
print(addresses)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(form_url)
driver.implicitly_wait(15)
address = driver.find_element(By.CSS_SELECTOR, value=".rFrNMe k3kHxc RdH0ib yqQS1 zKHdkd")

#address.click()
address.send_keys("hello my name is")
