# Udacity Project - Movie Trailer website

Note: the instructions below use commands ```python``` and ```pip```. Please replace these as appropriate depending on your python installation (e.g. ```python3``` or ```pip3```).

## Prerequisites
Note: The version requirements below are so strict because this project was built with specific versions of tools and libraries and has only been tested with those versions.

### Global
* python (v3.6.1)

### Installation
* wheel (v0.29.0): ```pip install 'wheel==0.29.0```

### Testing
* coverage (v4.4.1): ```pip install coverage==4.4.1```

### Execution
(requirements specified in the wheel)
* requests (v2.17.3): ```pip install requests==2.17.3```

## Distribution
To create distributable wheel, in the project root:
```
$> python setup.py bdist_wheel
```
This will create a ```dist``` directory and a wheel archive within it.

## Installation
To install the wheel:
```
$> pip install <wheel_file>
```
where ```<wheel_file>``` is the distribution wheel (see above).

## Usage
Once installed, usage can be found by running:
```
$> python -m movie_project -h
Usage: movie_project [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -d FILE, --data-file=FILE
                        reads movie specification from data file. JSON format
                        array containing object with keys 'title' and 'year'
```

To generate a static website containing default data:
```
$> python -m movie_project
```

This will generate  a file called ```fresh_tomatoes.html``` in the directory the above command was run, as well as the following progress output to console:

```
Disclaimer: This product uses the TMDb API but is not endorsed or certified by TMDb.
Retrieving film data...
Found: 'Unforgiven' (1992) -> Unforgiven (Some legends will never be forgotten. Some wrongs can never be forgiven.)
Found: 'Edge of Tomorrow' (2014) -> Edge of Tomorrow (Live, Die, Repeat)
Found: 'Ghostbusters' (2016) -> Ghostbusters (Who You Gonna Call?)
Found: 'Sunshine' (2007) -> Sunshine (If the sun dies, so do we.)
Found: 'Moana' (2016) -> Moana (The ocean is calling.)
Found: 'Alien' (1979) -> Alien (In space no one can hear you scream.)
Error: No data for 'dasdaasa' (100)
... retrieval complete.
```
Note that the ```Error:``` line is expected output and demonstrates how the application copes with data that can't be looked up.

To generate a static website containing custom data, provide a json file containing an array of film data:

```
$> python -m movie_project -d my_favorite_movies.json
Disclaimer: This product uses the TMDb API but is not endorsed or certified by TMDb.
Retrieving film data...
Found: 'unforgiven' (1992) -> Unforgiven (Some legends will never be forgotten. Some wrongs can never be forgiven.)
Found: 'starship troopers' (1997) -> Starship Troopers (The only good bug is a dead bug.)
Found: 'maltese falcon' (1941) -> The Maltese Falcon (A story as EXPLOSIVE as his BLAZING automatics!)
Found: 'pi' (1998) -> Pi (There will be no order, only chaos)
... retrieval complete.
```

where ```my_favorite_movies.json``` contained the following

```json
[
  {"title":"unforgiven", "year":1992},
  {"title":"starship troopers", "year":1997},
  {"title":"maltese falcon", "year":1941},
  {"title":"pi", "year":1998}
]
```


## Testing
To run tests, in the project root directory:
```
$> python setup.py test
```

To produce code coverage report, add the movie_project packge to your python library path, and from the project root directory:
```
$> coverage run -m unittest discover -s "test" -p "*_test.py"
.....................
----------------------------------------------------------------------
Ran 21 tests in 17.758s

OK

$> coverage report
Name                                           Stmts   Miss  Cover
------------------------------------------------------------------
src\movie_project\__init__.py                      1      0   100%
src\movie_project\media.py                         7      0   100%
src\movie_project\movie_data_reader.py             8      0   100%
src\movie_project\tmdbapi.py                      89      6    93%
test\movie_project\__init__.py                     1      0   100%
test\movie_project\media_test.py                  29      0   100%
test\movie_project\movie_data_reader_test.py      36      0   100%
test\movie_project\tmdbapi_test.py                75      0   100%
------------------------------------------------------------------
TOTAL                                            246      6    98%
```

## Revision History
* 1.1.0
 * can read movie data from file provided on command line
 * improved README.md
* 1.0.1
 * fixed issue with html file encoding being ascii instead of utf-8
* 1.0.0
 * first release
