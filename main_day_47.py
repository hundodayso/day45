from bs4 import BeautifulSoup
import requests
import smtplib
import keys

#url = "https://appbrewery.github.io/instant_pot/"
url =("https://www.amazon.co.uk/ring-battery-video-doorbell-plus/dp/B09WZBVWL9?ref="
      "dlx_deals_dg_dcl_B09WZBVWL9_dt_sl14_cf&pf_rd_r=7AMJ6ZZEDWNQAAEDF4A9&pf_rd_p"
      "=857a3987-6090-452e-aabb-77b2651d4dcf")

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}



response = requests.get(url, headers=header)

webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

#price = soup.select("div div span")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = float(price.split("£")[1])


print(price)

print(price_without_currency)

###SEND EMAIL HERE###

title = soup.find(id="productTitle").get_text().strip()
print(title)


if price_without_currency < 100:
    my_email = keys.email_addy
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=keys.email_addy, password=keys.email_app_pw)
    connection.sendmail(from_addr=keys.email_addy,
                        to_addrs=keys.to_email,
                        msg=f"Subject:Amazon Price Drop!\n\nPrice is less than 100! Click here to buy! {url}".encode("utf-8"))
    connection.close()