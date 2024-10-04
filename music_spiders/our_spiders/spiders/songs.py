import requests
import json
import os
from urllib.parse import urlparse

def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')

def get_playlist_tracks(playlist_id, access_token):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def extract_playlist_id(playlist_url):
    """Extracts the playlist ID from the Spotify playlist URL."""
    parsed_url = urlparse(playlist_url)
    return parsed_url.path.split('/')[-1]

def read_playlists_from_file(file_path):
    """Reads playlists from a .jl file and returns a list of (genre, playlist_url) tuples."""
    playlists = []
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return playlists

    with open(file_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                genre = data['genre']
                spotify_playlist_url = data['spotify_playlist_url']
                playlists.append((genre, spotify_playlist_url))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    return playlists

def save_to_jsonl(data, file_path):
    """Saves data to a .jl (JSON Lines) file."""
    with open(file_path, 'a') as f:
        f.write(json.dumps(data) + '\n')

def main():
    client_id = 'e95fb271927f4439a4ed2adf14b81989'  
    client_secret = 'c2158f55cdea43808d4dc89937bc1532'  
    file_path = "C:\\Users\\user\\Desktop\\music\\data\\playlist.jl"  
    output_file = "songs.jl" 

    access_token = get_access_token(client_id, client_secret)
    
    playlists = read_playlists_from_file(file_path)
    
    for genre, playlist_url in playlists:
        playlist_id = extract_playlist_id(playlist_url)
        tracks_data = get_playlist_tracks(playlist_id, access_token)

        songs = []
        for idx, item in enumerate(tracks_data.get('items', []), 1):
            track = item.get('track')
            if track:

                position = str(idx)
                name = track.get('name')
                artist = ', '.join([artist['name'] for artist in track.get('artists', [])])
                uri_id = track.get('uri')

                songs.append({
                    'position': position,
                    'name': name,
                    'artist': artist,
                    'uri_id': uri_id
                })

            if len(songs) >= 100:
                break

        playlist_data = {
            "songs": songs,
            "genre": genre
        }
        save_to_jsonl(playlist_data, output_file)
        
        print(f"Saved {len(songs)} songs for genre: {genre}")

if __name__ == "__main__":
    main()
