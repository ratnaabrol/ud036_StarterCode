"""Module that creates a static website showing favorite movies and their details."""
import pdb

import movie_project.media as media
import movie_project.fresh_tomatoes as fresh_tomatoes
import movie_project.tmdbapi as tmdbapi


"""The Movie data to be displayed on the web page."""
_MOVIE_DATA = [
    {"title": "Unforgiven", "year": 1992},
    {"title": "Edge of Tomorrow", "year": 2014},
    {"title": "Ghostbusters", "year": 2016},
    {"title": "Sunshine", "year": 2007},
    {"title": "Moana", "year": 2016},
    {"title": "Alien", "year": 1979},
    {"title": "dasdaasa", "year": 100},
]

def create_website(movie_data):
    """Creates a file called 'fresh_tomatoes.html' that contains the static
    movies website."""
    movies = []
    movie_api = tmdbapi.TmdbApi("1df9b566ca9b3dfab2e90488095ee920")
    print("Retrieving film data...")

    for movie_def in movie_data:
        movie_ids = movie_api.search(movie_def["title"], movie_def["year"])
        if len(movie_ids) > 0:
            movie_id = movie_ids[0] # use the id of the first movie returned
            movie = movie_api.movie(movie_id)
            trailer = ""
            trailers = movie_api.movie_trailer(movie_id)
            if (len(trailers) > 0):
                trailer = trailers[0]
            print("Found: '{}' ({}) -> {} ({})".format(movie_def["title"],
                                                  movie_def["year"],
                                                  movie["title"],
                                                  movie["tagline"]))
            movies.append(
                media.Movie(movie["title"],
                            movie["poster_url"],
                            trailer,
                            movie["tagline"],
                            movie["overview"]))
        else:
            print("Error: No data for '{}' ({})"
                            .format(movie_def["title"], movie_def["year"]))

    print("... retrieval complete.")

    fresh_tomatoes.open_movies_page(movies)
