import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

# Replace with your Spotify client ID, client secret, and redirect URI
auth_manager = SpotifyOAuth(client_id='3a353c7dc3ee4916bba070d176bffce1',
                            client_secret='2c30693d418b4de0bd9be73746a38d06',
                            redirect_uri='http://its-codee.com',
                            scope=['playlist-read-private', 'user-library-read'])

sp = spotipy.Spotify(auth_manager=auth_manager)
os.system('clear')
print(
"░██████╗██████╗░░█████╗░████████╗██╗███████╗██╗░░░██╗  ████████╗░█████╗░  ░░░████████╗██╗░░██╗████████╗\n"
"██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝╚██╗░██╔╝  ╚══██╔══╝██╔══██╗  ░░░╚══██╔══╝╚██╗██╔╝╚══██╔══╝\n"
"╚█████╗░██████╔╝██║░░██║░░░██║░░░██║█████╗░░░╚████╔╝░  ░░░██║░░░██║░░██║  ░░░░░░██║░░░░╚███╔╝░░░░██║░░░\n"
"░╚═══██╗██╔═══╝░██║░░██║░░░██║░░░██║██╔══╝░░░░╚██╔╝░░  ░░░██║░░░██║░░██║  ░░░░░░██║░░░░██╔██╗░░░░██║░░░\n"
"██████╔╝██║░░░░░╚█████╔╝░░░██║░░░██║██║░░░░░░░░██║░░░  ░░░██║░░░╚█████╔╝  ██╗░░░██║░░░██╔╝╚██╗░░░██║░░░\n"
)
print(
"This tool helps you with the tidious job of transfering songs from a streaming service to another,\n"
"by creating a full list of all songs you have in your playlist, despite the number of them.\n"
)
playlist_id = input("Enter the playlist ID (you find this in the playlist link. For example, the playlist ID for https://open.spotify.com/playlist/6nBPIX0KU3EoVLVylD5DKD it is 6nBPIX0KU3EoVLVylD5DKD): ")
expname = input("Enter the exported file name: ")

results = sp.playlist_tracks(playlist_id)
tracks = results['items']

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

with open(expname+'.txt', 'w') as f:
    f.write(
"░██████╗██████╗░░█████╗░████████╗██╗███████╗██╗░░░██╗  ████████╗░█████╗░  ░░░████████╗██╗░░██╗████████╗\n"
"██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝╚██╗░██╔╝  ╚══██╔══╝██╔══██╗  ░░░╚══██╔══╝╚██╗██╔╝╚══██╔══╝\n"
"╚█████╗░██████╔╝██║░░██║░░░██║░░░██║█████╗░░░╚████╔╝░  ░░░██║░░░██║░░██║  ░░░░░░██║░░░░╚███╔╝░░░░██║░░░\n"
"░╚═══██╗██╔═══╝░██║░░██║░░░██║░░░██║██╔══╝░░░░╚██╔╝░░  ░░░██║░░░██║░░██║  ░░░░░░██║░░░░██╔██╗░░░░██║░░░\n"
"██████╔╝██║░░░░░╚█████╔╝░░░██║░░░██║██║░░░░░░░░██║░░░  ░░░██║░░░╚█████╔╝  ██╗░░░██║░░░██╔╝╚██╗░░░██║░░░\n"
    )
    f.write(
"OpenAI test product. Follow me on instagram @codee_dev\n"
"(remove the text above if needed)\n\n\n"
    )
    for item in tracks:
        track = item['track']
        f.write(f'{track["name"]} - {track["artists"][0]["name"]}\n')

print(f'{len(tracks)} songs written to', expname+'.txt')
