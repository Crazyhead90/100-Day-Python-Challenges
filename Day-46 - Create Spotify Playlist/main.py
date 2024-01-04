import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "760f598a04e14b4da03eb41b7e3848dd"
Client_Secret = "3ea90c0c84284bf6b527e91983bdc4f7"

user_input = input("Which your do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{user_input}/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name='h3', class_="a-no-trucate")
song_titles = [song.getText().strip() for song in songs]

print(song_titles)

