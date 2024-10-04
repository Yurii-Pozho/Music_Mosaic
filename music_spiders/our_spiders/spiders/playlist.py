import json

with open(r"C:/Users/user/Desktop/music/data/genres.jl") as genres_file:
    playlists = []

    for line in genres_file:
        genre_data = json.loads(line.strip())  

        playlist = {
            "genre": genre_data["name"],
            "spotify_playlist_url": genre_data["url"].replace("https://embed.spotify.com/?uri=spotify:playlist:", "https://open.spotify.com/playlist/")
        }

        playlists.append(playlist)

with open('playlist.jl', 'w') as playlist_file:
    for playlist in playlists:
        playlist_file.write(json.dumps(playlist) + '\n')
