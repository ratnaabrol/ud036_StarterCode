import unittest
import movie_project.tmdbapi as tmdbapi
import threading

class TmdbApiTest(unittest.TestCase):

    _DEV_API_KEY = "1df9b566ca9b3dfab2e90488095ee920"

    # some test data
    _UNFORGIVEN_ID = 33
    _UNFORGIVEN_TITLE = "unforgiven"
    _UNFORGIVEN_YEAR = 1992
    _UNFORGIVEN_TRAILER = "ftTX4FoBWlE"

    def test_can_create_api(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        self.assertTrue(t.is_apikey_valid())

    def test_can_detect_invalid_api_key(self):
        t = tmdbapi.TmdbApi("Bad API Key")
        self.assertFalse(t.is_apikey_valid())

    def test_cannot_create_api_without_apikey(self):
        with self.assertRaises(TypeError):
            tmdbapi.TmdbApi()

    def test_search_with_valid_film_returns_ids(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        ids = t.search(TmdbApiTest._UNFORGIVEN_TITLE)
        self.assertGreater(len(ids), 0)

    def test_search_with_valid_film_in_year_return_correct_id(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        ids = t.search(TmdbApiTest._UNFORGIVEN_TITLE,
                       TmdbApiTest._UNFORGIVEN_YEAR)
        self.assertEqual(len(ids), 1)
        self.assertEqual(ids[0], TmdbApiTest._UNFORGIVEN_ID)

    def test_search_with_non_existent_film_returns_empty_list(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        ids = t.search("totally forgiven, eh?", 1010)
        self.assertEqual(len(ids), 0)

    def test_can_retrieve_movie_details_for_film(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        movie = t.movie(TmdbApiTest._UNFORGIVEN_ID)
        self.assertIsNotNone(movie)
        self.assertEqual(TmdbApiTest._UNFORGIVEN_ID, movie["id"])
        self.assertEqual(TmdbApiTest._UNFORGIVEN_TITLE.lower(),
                         movie["title"].lower())

    def test_has_poster_url_in_movie_details_for_valid_film(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        movie = t.movie(TmdbApiTest._UNFORGIVEN_ID)
        self.assertIsNotNone(movie["poster_url"])


    def test_none_returned_when_movie_query_is_given_bad_id(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        movie = t.movie(-1)
        self.assertIsNone(movie)

    def test_can_get_trailer_for_valid_film(self):
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        youtube_ids = t.movie_trailer(TmdbApiTest._UNFORGIVEN_ID)
        self.assertEqual(1, len(youtube_ids))
        self.assertEqual(TmdbApiTest._UNFORGIVEN_TRAILER, youtube_ids[0])


    def test_large_number_of_concurrent_api_calls_does_not_exceed_rate_limit(self):
        class SearchOp:
            '''Callable class to perform a search operation on tmdb'''
            def __init__(self, tester, api, search_term, on_success):
                self.tester = tester
                self.api = api
                self.search_term = search_term
                self.on_success = on_success

            def __call__(self):
                results = self.api.search(self.search_term)
                if len(results) > 0:
                    self.on_success()


        # initialise success count and maintain it in a thread safe manner
        success_count = 0
        success_lock = threading.Lock()
        def on_success():
            nonlocal success_count # used to allow us to modify success_count
                                   # as defined in outer scope
            with success_lock:
                success_count = success_count + 1

        # call the api concurrently
        thread_count = 50
        t = tmdbapi.TmdbApi(TmdbApiTest._DEV_API_KEY)
        threads = []
        for _ in range(thread_count):
            testing_thread = threading.Thread(
                              target=SearchOp(self, t,"Unforgiven", on_success))
            threads.append(testing_thread)
            testing_thread.start()

        # wait for the threads to complete
        for thread in threads:
            thread.join()

        # assert that each thread completed successfully
        self.assertEqual(thread_count, success_count)
