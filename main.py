from bs4 import BeautifulSoup
import requests
import keys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SP_CLIENT_ID = keys.client_id
SP_CLIENT_SECRET = keys.client_secret
SP_REDIRECT = keys.client_uri

#date = str(input("What year do you want to travel to? Type the date in format YYYY-MM-DD: "))
#url  = f"https://www.billboard.com/charts/hot-100/{date}/"


scope = "user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_CLIENT_ID,
                                               client_secret=SP_CLIENT_SECRET, redirect_uri=SP_REDIRECT, scope=scope))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

user = sp.currently_playing()
print(user)




# url = f"https://www.billboard.com/charts/hot-100/2012-10-10/"
#
#
# # header = {
# #     "User=Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
# # }
#
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
#
# response = requests.get(url, headers=header)
# #print(response)
#
# billboard_webpage = response.text
# #print(billboard_webpage)
#
# soup = BeautifulSoup(billboard_webpage, 'html.parser')
#
# song_list = soup.select("li ul li h3")
#
# songs = [song_name.getText().strip() for song_name in song_list]
# print(songs)

#songs = [song_name.getText().strip() for song_name in soup.find_all(name="h3", class_=lambda value: value and value.startswith("c-title"))]

#songs = [song_name.getText() for song_name in soup.find_all(name="h3", id="title-of-a-story")]
