# Udacity Project - Movie Trailer website

## Prerequisites
Note: The version requirements below are so strict because this project was built with specific versions of tools and libraries and has only been tested with those versions.

* python (v3.6.1)
* wheel (v0.29.0): ```pip install 'wheel==0.29.0```
* coverage (v4.4.1): ```pip install coverage==4.4.1```
* TBC...

## Distribution
To create wheel:
```
$> python setup.py bdist_wheel
```

## Testing
To run tests:
```
$> python setup.py test
```

To produce code coverage report:
```
$> coverage run -m unittest discover -s "test" -p "*_test.py"
...
$> coverage html
```
