import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

films = [headline.getText() for headline in soup.find_all(name="h3", class_="title")]
films.reverse()
print(films)

with open("films.txt", 'w', encoding='utf-8') as f:
    for film in films:
        f.write(film)
        f.write("\n")


