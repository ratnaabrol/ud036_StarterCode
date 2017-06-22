"""Main script for the package. Will create a static website based on the
default data held within this package."""

import movie_project.entertainment_center as ec
print("Disclaimer: This product uses the TMDb API but is not endorsed or certified by TMDb.")
ec.create_website(ec._MOVIE_DATA)
