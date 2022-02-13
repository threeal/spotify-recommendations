# Spotify Recommendations

This project could give user a recommendation through a playlist.

## Setup

- Install Python [here](https://www.python.org/downloads/).
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
- Create a new spotify app if you don't have one (see [this](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/)
- Create a `.env` file with the following content:
  ```
  SPOTIPY_CLIENT_ID=YOUR_APP_CLIENT_ID
  SPOTIPY_CLIENT_SECRET=YOUR_APP_CLIENT_SECRET
  ```

## Usage

### Get Artist by Tracks

run `python get_artist_by_tracks.py --help` for more details
```sh
python get_artist_by_tracks.py 'track name' 'other track name' ...
```
