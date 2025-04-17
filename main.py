from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
URL = "https://orteil.dashnet.org/experiments/cookie/"
TIME_TO_PLAY = 30
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
game_on = True


cookie = driver.find_element(By.ID, value="cookie")
start_time = time.time()
old_time = time.time()

store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store]
#print(item_ids)


#while loop to do bits
while game_on:
    cookie.click()

    money = driver.find_element(By.ID, value="money")
    time_now = time.time()

    if time_now - old_time >= 5:

        store_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')


        old_time = time.time() #set the old to the time now
    if time_now - start_time >= TIME_TO_PLAY: #check if exceeded play time
        print("Game Ending...")
        game_on = False


# for i in range(10):
#     cookie.click()
#
#     print(money.text)
