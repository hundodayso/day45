from bs4 import BeautifulSoup
import requests
import spotipy

from spotipy.oauth2 import SpotifyOAuth
import keys

spotify_ep = "https://api.spotify.com/v1/search"
SP_CLIENT_ID = keys.client_id
SP_CLIENT_SECRET = keys.client_secret
SP_REDIRECT = keys.redirect

scope = "playlist-modify-private"

date = str(input("What year do you want to travel to? Type the date in format YYYY-MM-DD: "))
date = date.strip('-')
url  = f"https://www.billboard.com/charts/hot-100/{date}/"
#date = "2012-10-10"
#url = f"https://www.billboard.com/charts/hot-100/2012-10-10/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url, headers=header)

billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, 'html.parser')

song_list = soup.select("li ul li h3")

songs = [song_name.getText().strip() for song_name in song_list]
print(songs)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_CLIENT_ID,
                                               client_secret=SP_CLIENT_SECRET,
                                               redirect_uri=SP_REDIRECT,
                                               scope=scope
                                               ))

#


####Example Song Response#
# song_response = sp.search('https://api.spotify.com/v1/search?q=remaster%252'
#                           '0track%3ADoxy%2520artist%3AMiles%2520Davis&type=album&market=UK&limit=2')

track_uris = []

for song in songs:
    q = f"track:{song} year:{date[:4]}"
    try:
        song_response = sp.search(q=q, limit=1, type="track", market="GB", offset=0)
        print(song_response)
        track_uris.append(song_response["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"Song {song} not available")

print(track_uris)
playlist_name = f"Billboardd 100 songs of {date}"
user = sp.current_user()["id"]
print(user)
new_playlist = sp.user_playlist_create(user=user, name=playlist_name, public=False, collaborative=False, description=f"Playlist of the Billboard 100 for {date}")
sp.playlist_add_items(playlist_id=new_playlist["id"], items=track_uris)



