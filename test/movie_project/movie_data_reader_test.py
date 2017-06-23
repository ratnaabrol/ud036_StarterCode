"""Unit tests for the movie_data_reader module."""

import unittest
import io
import json

import movie_project.movie_data_reader as movie_data_reader

class MovieDataTest(unittest.TestCase):

    def test_throws_exception_when_reading_invalid_json(self):
        with io.StringIO("bad json") as invalid_stream:
            with self.assertRaises(json.decoder.JSONDecodeError):
                movie_data_reader.movie_data_from_json(invalid_stream)

    def test_returns_correct_data_when_reading_valid_movie_data_json(self):
        with io.StringIO('[{"title":"hello", "year":1212},{"title":"bye", "year":698}]') as valid_stream:
            data = movie_data_reader.movie_data_from_json(valid_stream)
            self.assertIn("title", data[0])
            self.assertIn("year", data[0])
            self.assertEqual("hello", data[0]["title"])
            self.assertEqual(1212, data[0]["year"])
            self.assertIn("title", data[1])
            self.assertIn("year", data[1])
            self.assertEqual("bye", data[1]["title"])
            self.assertEqual(698, data[1]["year"])

    def test_ignores_invalid_extra_keys_when_reading_movie_data_json(self):
        with io.StringIO('[{"title":"hello", "ignore":"me", "year":1212}]') as valid_stream:
            data = movie_data_reader.movie_data_from_json(valid_stream)
            self.assertIn("title", data[0])
            self.assertIn("year", data[0])
            self.assertNotIn("ignore", data[0])
            self.assertEqual("hello", data[0]["title"])
            self.assertEqual(1212, data[0]["year"])

    def test_ignores_invalid_objects_when_reading_movie_data_json(self):
        with io.StringIO('[{"bad":"hello"},{"title":"hello", "year":1212}]') as valid_stream:
            data = movie_data_reader.movie_data_from_json(valid_stream)
            self.assertEqual(1, len(data))
            self.assertIn("title", data[0])
            self.assertIn("year", data[0])
            self.assertEqual("hello", data[0]["title"])
            self.assertEqual(1212, data[0]["year"])
