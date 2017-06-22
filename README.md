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

## Execution
Once installed a static website containing default data can be generated:
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

## Testing
To run tests:
```
$> python setup.py test
```

To produce code coverage report (below expects movie_project to be on your system path):
```
$> coverage run -m unittest discover -s "test" -p "*_test.py"
...
$> coverage html
```

## Revision History
* 1.0.0
 * first release
* 1.0.1
 * fixed issue with html file encoding being ascii instead of utf-8
