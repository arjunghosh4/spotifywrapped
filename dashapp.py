import dash
from dash import dcc, html
import plotly.express as px
from spotifydata import get_data
from visualizations import plot_top_tracks, plot_top_genres

# Fetch Data
tracks_df, artists_df, albums_df, genre_counts = get_data()

# Generate Figures
fig_tracks = plot_top_tracks(tracks_df)

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout with styling
app.layout = html.Div(
    style={
        "font-family": "Arial, sans-serif", 
        "background-color": "#f0f0f0", 
        "padding": "20px"
    },
    children=[
        html.H1("Spotify 2024 Wrapped: Year in Review", 
                style={"text-align": "center", "color": "#1DB954", "margin-bottom": "30px"}),

        # Layout for top tracks
        html.Div(
            style={"display": "flex", "justify-content": "center", "margin-bottom": "50px"},
            children=[
                dcc.Graph(figure=fig_tracks, style={"height": "450px", "width": "80%"})
            ]
        ),

        # Example of top artist stats (add more visualizations as needed)
        html.Div(
            children=[
                html.H2("Top Artists", style={"text-align": "center", "color": "#333"}),
                html.Div(
                    children=[html.Div(f"{i+1}. {artist['name']} - Genres: {', '.join(artist['genres'])}") 
                              for i, artist in enumerate(artists_df.to_dict('records'))],
                    style={"padding": "20px", "border": "1px solid #ddd", "border-radius": "10px", "max-height": "300px", "overflow-y": "auto"}
                )
            ],
            style={"text-align": "center", "margin-top": "30px"}
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
