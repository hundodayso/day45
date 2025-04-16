from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

element = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]')
event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li a")

events = {}
print(len(event_names))
for i in range(len(event_names)):
    events[i] = {
        "time": event_dates[i].text.split("T")[0],
        "name": event_dates[i].text
    }

print(events)

