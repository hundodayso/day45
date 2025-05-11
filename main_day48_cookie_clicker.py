from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
URL = "https://orteil.dashnet.org/experiments/cookie/"
TIME_TO_PLAY = 30
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
game_on = True



start_time = time.time()
old_time = time.time()

##get the IDs of the items in the store###

store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store]
item_ids.pop()
item_ids.reverse()
print(item_ids)



###while loop to do bits
while game_on:

    #keep clicking!
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

    #determine the time
    time_now = time.time()

    if time_now - old_time >= 5:

        ##start getting prices
        store_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        usable_prices = []
        for item in store_prices:
            if item.text != "":
                actual_price = item.text.split("- ")[1].replace(",", "")
                #print(actual_price)
                usable_prices.append(actual_price)

        money_in_bank = driver.find_element(By.ID, value="money").text
        if "," in money_in_bank:
            money_in_bank = money_in_bank.replace(",","")
        cookie_count = int(money_in_bank)


        ##check prices of store to buy
        for idx, purchase_price in enumerate(reversed(usable_prices)):
            if cookie_count > int(purchase_price):
                purchase_id = item_ids[idx]
                print(purchase_id)
                break
        driver.find_element(By.ID, value=purchase_id).click()

        old_time = time.time()
    if time_now - start_time >= TIME_TO_PLAY: #check if exceeded play time
        print("Game Ending...")
        game_on = False



