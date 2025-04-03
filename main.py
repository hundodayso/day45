from bs4 import BeautifulSoup
import requests

#response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="span", class_="titleline")
print(article_tag)
article_text = article_tag.getText()
print(f"{article_text = }")

article_link = article_tag.select_one(selector=".titleline a").get("href")
print(article_link)
article_upvote = soup.find(name="span", class_="score").getText()
print(f"{article_upvote = }")
