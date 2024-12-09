import pandas as pd
from auth import authenticate_spotify

def get_top_tracks(sp, limit=50, time_range='long_term'):
    return sp.current_user_top_tracks(limit=limit, time_range=time_range)

def get_top_artists(sp, limit=50, time_range='long_term'):
    return sp.current_user_top_artists(limit=limit, time_range=time_range)

def get_saved_albums(sp, limit=50):
    return sp.current_user_saved_albums(limit=limit)

def process_top_artists(top_artists):
    artists_df = pd.DataFrame(top_artists['items'], columns=['name', 'genres'])
    top_genres = []
    for artist in artists_df['genres']:
        top_genres.extend(artist)
    
    genre_counts = pd.Series(top_genres).value_counts()

    # Save the artists DataFrame and top genres as CSV
    artists_df.to_csv('data/top_artists.csv', index=False)  # Export top artists

    # Convert the genre counts to a DataFrame for easy visualization
    top_genres_df = pd.DataFrame(genre_counts).reset_index()
    top_genres_df.columns = ['Genre', 'Count']
    top_genres_df.to_csv('data/top_genres.csv', index=False)  # Save top genres as CSV

    return artists_df, genre_counts

def process_top_tracks(top_tracks):
    tracks_df = pd.DataFrame(top_tracks['items'], columns=['name', 'artists', 'album', 'popularity', 'duration_ms'])
    tracks_df['artists'] = tracks_df['artists'].apply(lambda x: x[0]['name'])  # Get artist names
    tracks_df.to_csv('data/top_tracks.csv', index=False)  # Export top tracks
    return tracks_df

def process_saved_albums(saved_albums):
    albums_data = []
    for item in saved_albums['items']:
        album = item['album']
        album_data = {
            'name': album['name'],
            'artist': ', '.join([artist['name'] for artist in album['artists']]),
            'release_date': album['release_date'],
            'id': album['id']
        }
        albums_data.append(album_data)
    albums_df = pd.DataFrame(albums_data)
    albums_df.to_csv('data/saved_albums.csv', index=False)  # Export saved albums
    return albums_df

def get_data():
    sp = authenticate_spotify()
    top_tracks = get_top_tracks(sp)
    top_artists = get_top_artists(sp)
    saved_albums = get_saved_albums(sp)

    artists_df, genre_counts = process_top_artists(top_artists)
    tracks_df = process_top_tracks(top_tracks)
    albums_df = process_saved_albums(saved_albums)

    return tracks_df, artists_df, albums_df, genre_counts

if __name__ == "__main__":
    tracks_df, artists_df, albums_df, genre_counts = get_data()
    print(tracks_df.head())
    print(artists_df.head())
    print(albums_df.head())
    print(genre_counts.head())
