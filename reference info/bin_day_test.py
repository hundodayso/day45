from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, datetime

import keys

url = "https://mycouncil.milton-keynes.gov.uk/service/Waste_Collection_Round_Checker"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)


element = driver.find_element(By.XPATH, '//*[@id="btn-anon"]')
element.click()
driver.implicitly_wait(15)
driver.switch_to.frame("fillform-frame-1")

###next page##

#postcode = driver.find_element(By.XPATH, '//*[@id="postcode_search"]')
postcode = driver.find_element(By.ID, value="postcode_search")
#print(postcode)
postcode.clear()
postcode.send_keys(keys.postcode)
driver.implicitly_wait(5)
address = Select(driver.find_element(By.ID, value="ChooseAddress"))
address.select_by_visible_text(keys.addy)

wait = WebDriverWait(driver, 10)
#bins = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="AF-Form-1a083dbd-80dd-4a81-8e7e-7ab0b66b5fb5"]/section[2]/section/div[16]/div/span/table/tbody/tr[2]/td[5]')))
tbody = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody")))

rows = tbody.find_elements(By.TAG_NAME, "tr")
bins = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    td_texts = [cell.get_attribute("textContent").strip() for cell in cells]
    #print(td_texts)
    last_word = td_texts[5].strip().split()[-1].lower()

    # print(f"Bin: {td_texts[5]}")
    # print(f"Date:{td_texts[9]}")
    if last_word == "red" or last_word =="blue":
        bins.append([last_word, td_texts[9]])


today = date.today()
for bintype in bins:
    converted_date = datetime.strptime(bintype[1], "%Y-%m-%d").date()
    delta = converted_date - today
    days_to = delta.days
    if days_to < 7:
        bin_colour = bintype[0].capitalize()
        print(bin_colour)








