class Movie:
    """Entity representing the concept of a movie."""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
         """Movie constructor.

         Keyword arguments:
         title -- the title of the movie. Must be provided by the caller.
         poster_image_url -- the url to the movie poster. Must be provided by the caller.
         trailer_youtube_url -- the url to the trailer for this movie on YouTube. Must be provided by the caller.
         """
         self.title = title
         self.poster_image_url = poster_image_url
         self.trailer_youtube_url = trailer_youtube_url
