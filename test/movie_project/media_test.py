"""Test cases for the media module."""

import unittest
import movie_project.media as media

class MediaTest(unittest.TestCase):

    def test_can_create_valid_movie(self):
        m = media.Movie("title", "poster", "trailer")
        self.assertEqual(m.title, "title")
        self.assertEqual(m.poster_image_url, "poster")
        self.assertEqual(m.trailer_youtube_url, "trailer")

    def test_cannot_create_movie_without_title(self):
        with self.assertRaises(TypeError):
            m = media.Movie(poster_image_url="poster", trailer_youtube_url="trailer")

    def test_cannot_create_movie_without_poster(self):
        with self.assertRaises(TypeError):
            m = media.Movie(title="title", trailer_youtube_url="trailer")

    def test_cannot_create_movie_without_trailer(self):
        with self.assertRaises(TypeError):
            m = media.Movie(title="title", poster_image_url="poster")
