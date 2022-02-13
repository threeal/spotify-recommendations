import argparse
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load client id and secret
load_dotenv()

# parse arguments
parser = argparse.ArgumentParser(description='get artist details by tracks')
parser.add_argument('tracks', nargs='+', help='list of tracks')
args = parser.parse_args()

# setup spotify client
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

for track in args.tracks:
    results = spotify.search(track, limit=1, type='track')

    if 'tracks' not in results:
        continue
    if 'items' not in results['tracks']:
        continue
    tracks = results['tracks']['items']

    if len(tracks) < 1:
        continue
    track = tracks[0]

    if 'name' not in track:
        continue
    print('%s:' % (track['name']))

    if 'artists' not in track:
        continue
    artists = track['artists']

    if len(artists) < 1:
        print('- no artist')
        continue

    for artist in artists:
        if 'name' not in artist:
            print('- unknown artist')
            continue

        print('- %s' % artist['name'])
