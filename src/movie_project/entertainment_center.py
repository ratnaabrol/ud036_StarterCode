"""Module that creates a static website showing favorite movies and their details."""

import movie_project.media as media
import movie_project.fresh_tomatoes as fresh_tomatoes

"""The Movie data to be displayed on the web page."""
MOVIE_DATA = [
    {"title": "Unforgiven",
     "poster": "https://upload.wikimedia.org/wikipedia/en/4/4e/Unforgiven_2.jpg",
     "trailer": "https://www.youtube.com/watch?v=ftTX4FoBWlE"},
    {"title": "Edge of Tomorrow",
     "poster": "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
     "trailer": "https://www.youtube.com/watch?v=yUmSVcttXnI"},
    {"title": "Ghostbusters (2016)",
     "poster": "https://upload.wikimedia.org/wikipedia/en/3/32/Ghostbusters_2016_film_poster.png",
     "trailer": "https://www.youtube.com/watch?v=w3ugHP-yZXw"},
    {"title": "Sunshine (2007)",
     "poster": "https://upload.wikimedia.org/wikipedia/en/6/68/Sunshine_poster.jpg",
     "trailer": "https://www.youtube.com/watch?v=r8BSlqHAhuY" }

]

def create_website():
    """Creates a file called 'fresh_tomatoes.html' that contains the static movies website."""
    movies = []
    for movie_def in MOVIE_DATA:
        movies.append(media.Movie(movie_def["title"], movie_def["poster"], movie_def["trailer"]))
    fresh_tomatoes.open_movies_page(movies)
