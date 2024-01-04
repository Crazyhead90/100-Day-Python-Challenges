import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie_titles = [movies.getText() for movies in soup.find_all(name="h3")]

movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")


#---------- Training ----------#

# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/")
#
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
# articles = soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# # print(article_texts)
# # print(article_links)
# # print(article_upvotes)
#
# highest_votes = article_upvotes.index(max(article_upvotes))
#
# print(article_texts[highest_votes])
# print(article_links[highest_votes])
# # print(article_upvotes[highest_votes])
