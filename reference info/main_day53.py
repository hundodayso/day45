from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

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
#driver.implicitly_wait(15)

length_of_loop = len(links)

for i in range(length_of_loop):

    input_address = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    #address = driver.find_element(By.CSS_SELECTOR, value="#whsOnd zHQkBf")
    if addresses[i]:
        input_address.send_keys(addresses[i])
    else:
        input_address.send_keys("Placeholder")

    input_price = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    if prices_as_string[i]:
        input_price.send_keys(prices_as_string[i])
    else:
        input_price.send_keys("Placeholder")


    input_link = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    if links[i]:
        input_link.send_keys(links[i])
    else:
        input_link.send_keys("Placeholder")

    submit_button = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    submit_button.click()
    driver.implicitly_wait(3)
    submit_another_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    submit_another_button.click()
    driver.implicitly_wait(10)
