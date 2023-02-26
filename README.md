# spotify-to-text
A simple way to convert your spotify playlist to a text document

#What it is?
The script utilizes the SpotifyOAuth authentication flow to obtain an access token, which allows the user to retrieve information about their Spotify account, such as their playlists and the tracks within those playlists.

The script can be run from the command line, with the user providing their client ID, client secret, and redirect URI as arguments. Once authenticated, the user can specify a playlist ID to retrieve the tracks within that playlist. The script then retrieves the track information and writes it to a text file named "songs.txt".

The script makes use of the Spotipy library to simplify interactions with the Spotify Web API. The library provides functions for retrieving various types of data from the API, such as user information, playlists, tracks, and albums. The library also handles the authentication flow required by the Spotify Web API.

The authentication flow used by the script is the SpotifyOAuth flow, which requires the user to provide their client ID, client secret, and redirect URI. The flow allows the user to grant the script access to their Spotify account, which allows the script to interact with their account and retrieve information about their playlists and tracks.

#Installing

