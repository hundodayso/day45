from bs4 import BeautifulSoup
import requests

#response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
print(articles)
article_texts = []
article_links = []

for article_tag in articles:

    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.select_one(selector=".titleline a").get("href")
    article_links.append(article_link)


print(f"{article_texts = }")
print(f"{article_links}")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(f"{article_upvotes = }")

index_highest_value = article_upvotes.index(max(article_upvotes))
print(f"{article_texts[index_highest_value]} + {article_links[index_highest_value]} + {article_upvotes[index_highest_value]}")