"""This is a very simple API to The Movie Database. There are already other APIs
available and this implementation has been implemented as an exercise in
understanding how to interact with an web API in Python.

This product uses the TMDb API but is not endorsed or certified by TMDb
(https://www.themoviedb.org/documentation/api/terms-of-use)."""

import requests
import time
import threading

TMDB_API_URL_PATTERN=r"https://api.themoviedb.org/3/{method}"

class TmdbApi:

    _MAX_REQUEST_RETRIES = 5

    def __init__(self, api_key):
        """Constructor.

        Keyword arguments:
        apikey -- the TMDb API key that authorises use of the TMDb API. Must be
                  provided by the caller.
        """
        self._api_key = api_key
        self._got_config = False
        self._unauthorised_lock = threading.Lock()
        self._unauthorised = True
        self._config_lock = threading.Lock()
        self._config = {};
        self._cache_configuration()

    def is_apikey_valid(self):
        """Returns whether we can access the TMDb API using the api key supplied
        in the constructor.

        This is implemented by attempting to call the configuration
        method on the api."""
        got_config = self._cache_configuration();
        return got_config == True and self._unauthorised == False

    def search(self, name, year=None):
        """Search for a film by name and optionally year.

        Returns a list of ids matching the search parameters, or an empty
        list if there is no match or the search fails.

        Keyword arguments:
        name -- the name to search for. Must be provided by the caller.
        year -- the year in which the movie was released. Optional.
        """
        found_ids = [];

        if not self._cache_configuration():
            return found_ids

        params = {"query":name}
        if year is not None:
            params["year"] = year
        search_response = self._call_tmdbapi("search/movie", params)

        if search_response.status_code != 200:
            return found_ids

        search_results = search_response.json()["results"]
        for result in search_results:
            found_ids.append(result["id"])
        return found_ids

    def movie(self, id):
        """Get the details for a single movie.

        Returns the movie details, or None if no such movie exists.
        The returned movie details are a dictionary matching the tmdbapi
        movie object, with one exception: it includes a 'poster_url' key.

        Keyword arguments:
        id -- the details of the movie. Must be provided by the caller.
        """
        movie = None
        if not self._cache_configuration():
            return movie

        movie_response = self._call_tmdbapi("movie/{}".format(id))

        if movie_response.status_code != 200:
            return movie

        movie = movie_response.json().copy()
        # add poster url
        if movie["poster_path"] is not None:
            with self._config_lock:
                movie["poster_url"] = "{}w500{}".format(
                                                    self._config["image_url"],
                                                    movie["poster_path"])
        else:
            movie["poster_url"] = None

        return movie

    def movie_trailer(self, id):
        """Get youtube id(s) for trailer(s) for a single movie.

        Returns a list of youtube ids, or an empty list if there are no trailers
        or the movie does not exist.

        Keyword arguments:
        id -- the details of the movie. Must be provided by the caller.
        """
        youtube_ids = []
        if not self._cache_configuration():
            return youtube_ids

        videos_response = self._call_tmdbapi("movie/{}/videos".format(id))

        if videos_response.status_code != 200:
            return youtube_ids

        videos = videos_response.json()["results"]
        for video in videos:
            if (video["type"].lower() == "trailer" and
                video["site"].lower() == "youtube"):
                youtube_ids.append(video["key"])
        pass

        return youtube_ids


    def _call_tmdbapi(self, method_to_call, method_params={}):
        augmented_params = method_params.copy();
        augmented_params["api_key"] = self._api_key;
        send_request = True
        retry_count = 0
        while send_request and retry_count < TmdbApi._MAX_REQUEST_RETRIES:
            response = requests.get(
                            TMDB_API_URL_PATTERN.format(method=method_to_call),
                            params=augmented_params)
            if response.status_code == 429:
                self._impose_call_rate_limit(response)
                send_request = True
                retry_count = retry_count + 1
            else:
                self._check_for_global_response_errors(response)
                send_request = False

        return response

    def _check_for_global_response_errors(self, response):
        with self._unauthorised_lock:
            self._unauthorised = (response.status_code == 401)

    def _impose_call_rate_limit(self, response):
        next_call_in = int(response.headers["Retry-After"]) # in seconds
        if next_call_in <= 0:
            return
        else:
            time.sleep(next_call_in)

    def _cache_configuration(self):
        """Lazy caching of tmdb configuration."""
        got_config = None

        with self._config_lock: # brute force, but will do for now
            if not self._got_config:
                config = self._call_tmdbapi("configuration")
                if config.ok:
                    self._got_config = True
                    self._config["image_url"] = \
                        config.json()["images"]["base_url"]
                else:
                    self._got_config = False

            got_config = self._got_config

        return got_config
