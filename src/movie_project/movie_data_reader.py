"""Utilities for reading movie data from file"""

import json

def movie_data_from_json(stream):
    """Reads movie data from stream as json and returns valid data.
    Any invalid data (note not invalid json) in the stream is ignored.

    Keyword arguments:
    stream -- a file like stream object containing json data

    Raises:
    json.decoder.JSONDecodeError -- when stream contains invalid json
    """
    movie_json = json.load(stream)

    movie_data = []
    for item in movie_json:
        if "title" in item and "year" in item:
            # copy only the data we need out of the json
            movie_data.append({"title": item["title"], "year": item["year"]})

    return movie_data
