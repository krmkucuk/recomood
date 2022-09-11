import json
import time
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import random

client_id = '2d5fab86e45744328c7245fbbca349a9'
client_secret = 'b366932953fc4730aa29f70fc65d675c'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager =client_credentials_manager)


#func to extract all track ids

def get_track_ids(playlist_id):
    music_id_list = []
    playlist = sp.playlist(playlist_id)

    for item in playlist['tracks']['items']:
        music_track = item['track']
        music_id_list.append(music_track['id'])
    return music_id_list

#get the ids for all songs

playlist_id = input('Enter the playlist id')
track_ids = get_track_ids(playlist_id)

random.shuffle(track_ids)

embed = '<iframe src="https://open.spotify.com/embed/track/{}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

print(embed)






