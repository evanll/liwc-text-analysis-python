[![Build Status](https://travis-ci.org/evanll/liwc-text-analysis-python.svg?branch=master)](https://travis-ci.org/evanll/liwc-text-analysis-python)

# LIWC Text Analysis - Python
A python package for the Linguistic Inquiry and Word Count (LIWC) dictionary. This package requires the proprietary LIWC dictionary file (.dic), that can be obtained from [LIWC.net](http://liwc.net/). 

## Usage
```python
>>> from liwc import Liwc
>>> liwc = Liwc(LIWC_FILEPATH)
>>> # Search a word in the dictionary to find in which LIWC categories it belongs
>>> print(liwc.search('happy'))
['affect', 'posemo']
>>> # Extract raw counts of words in a document that fall into the various LIWC categories
>>> print(liwc.parse('I love ice cream.'.split(' ')))
Counter({'verb': 1, 'present': 1, 'affect': 1, 'posemo': 1, 'bio': 1, 'sexual': 1, 'social': 1})
```
## Tests
The project comes with an extensive set of unit tests. The Pytest framework is used for unit testing. 
To run the tests use:  
`pytest`

## Project repository
https://github.com/evanll/liwc-text-analysis-python

## Author
Written by Evan Lalopoulos <evan.lalopoulos.2017@my.bristol.ac.uk>

**Evan Lalopoulos** - [evanll](https://github.com/evanll)
