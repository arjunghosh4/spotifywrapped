import plotly.express as px
import pandas as pd

# Function to plot top tracks
def plot_top_tracks(tracks_df):
    fig = px.bar(tracks_df, x='name', y='popularity', title='Top Tracks of the Year', labels={'name': 'Track Name', 'popularity': 'Popularity'})
    return fig

# Function to plot top genres
def plot_top_genres(genre_df):
    fig = px.pie(genre_df, names=genre_df.Genre, values=genre_df.Count, title='Top Genres of the Year')
    return fig

# Function to plot top artists
def plot_top_artists(artists_df):

    top_artists = artists_df.head()  # Get top 5 artists by count
    top_artists.columns = ['Artist', 'Genre']  # Renaming columns for clarity

    # Step 3: Create the plot
    fig = px.bar(top_artists, x='Artist', title='Top 5 Artists of the Year', labels={'Artist': 'Artist Name'})

    #fig = px.bar(artists_df, x='name', y='genres', title='Top Artists of the Year', labels={'name': 'Artist Name', 'genres': 'Genres'})
    return fig

if __name__ == "__main__":
    # Reading the CSV files generated by spotifydata.py
    tracks_df = pd.read_csv('data/top_tracks.csv')
    artists_df = pd.read_csv('data/top_artists.csv')
    genre_df = pd.read_csv('data/top_genres.csv')

    # Create visualizations
    fig_tracks = plot_top_tracks(tracks_df)
    fig_genres = plot_top_genres(genre_df)
    fig_artists = plot_top_artists(artists_df)

    # Display the figures
    fig_tracks.show()
    fig_genres.show()
    fig_artists.show()