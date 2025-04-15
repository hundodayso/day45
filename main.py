from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

element = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]')
event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li a")


events = []
for i in range(len(event_names)):
   event_date = event_dates[i].text.split("T")[0]
   event_name = event_names[i].text
   event = [event_date, event_name]
   events.append(event)

print(events)








