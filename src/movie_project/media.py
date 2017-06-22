class Movie:
    """Entity representing the concept of a movie."""

    def __init__(self, title, poster_image_url, trailer_youtube_key, tagline="", storyline=""):
         """Movie constructor.

         Keyword arguments:
         title -- the title of the movie. Must be provided by the caller.
         poster_image_url -- the url to the movie poster. Must be provided by
            the caller.
         trailer_youtube_key -- the YouTube key for this movie's trailer on
            YouTube. Must be provided by the caller.
         tagline -- a tagline for the movie. Optional.
         storyline -- the movie's storyline. Optional.
         """
         self.title = title
         self.poster_image_url = poster_image_url
         self.trailer_youtube_key = trailer_youtube_key
         self.tagline = tagline
         self.storyline = storyline
