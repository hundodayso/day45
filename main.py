from bs4 import BeautifulSoup
import requests

date = str(input("What year do you want to travel to? Type the date in format YYYY-MM-DD: "))
url  = f"https://www.billboard.com/charts/hot-100/{date}/"

#url = f"https://www.billboard.com/charts/hot-100/2012-10-10/"

print(url)

# header = {
#     "User=Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
# }

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url, headers=header)
print(response)

billboard_webpage = response.text
#print(billboard_webpage)

soup = BeautifulSoup(billboard_webpage, 'html.parser')

songs = [song_name.getText() for song_name in soup.find_all(name="h3", id="title-of-a-story")]
print(songs)