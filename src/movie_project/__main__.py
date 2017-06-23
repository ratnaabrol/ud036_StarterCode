"""Main script for the package. Will create a static website based on the
default data held within this package."""

from optparse import OptionParser
import json
import sys

import movie_project.entertainment_center as ec
import movie_project.movie_data_reader as movie_data_reader

parser = OptionParser(prog="movie_project", version="%prog v1.1.0") # TODO: auto sync with setup.py
parser.add_option("-d", "--data-file",
                  action="store",
                  type="string",
                  dest="data_filename",
                  help="reads movie specification from data file. JSON format array containing object with keys 'title' and 'year'",
                  metavar="FILE");

(options, args) = parser.parse_args()

movie_data = None
abnormal_exit = False
if options.data_filename is not None:
    try:
        with open(options.data_filename, "r") as data_file:
            movie_data = movie_data_reader.movie_data_from_json(data_file)
    except FileNotFoundError:
        print("Error: Unable to open data file: {}".format(options.data_filename))
        abnormal_exit = True
    except json.decoder.JSONDecodeError as err:
        print("Error: Invalid JSON in data file: {} ({})".format(options.data_filename, err.msg))
        abnormal_exit = True

if abnormal_exit:
    print()
    parser.print_help()
    sys.exit()

if movie_data is None:
    movie_data = ec._MOVIE_DATA

print("Disclaimer: This product uses the TMDb API but is not endorsed or certified by TMDb.")
ec.create_website(movie_data)
