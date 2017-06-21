from setuptools import setup, find_packages
import unittest

# configure test discovery
TEST_DIR = "test"
TEST_PATTERN = "*_test.py"


def test_suite():
    '''Creates test suite using the unittest's discovery algorithm.'''
    loader = unittest.TestLoader()
    suite = loader.discover(TEST_DIR, TEST_PATTERN)
    return suite

setup(
    name = "Movie Website Project",
    version = "0.1",
    packages = find_packages("src"),
    package_dir={"":"src"},
    test_suite = "setup.test_suite"
)
