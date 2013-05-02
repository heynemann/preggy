preggy
======

[![Build Status](https://travis-ci.org/heynemann/preggy.png?branch=master)](https://travis-ci.org/heynemann/preggy)

preggy is a collection of expectations for python applications, extracted from the pyVows project.

Usage
-----

Using preggy is very simple:
```python
from preggy import expect

def test_roses_are_red():
    rose = Rose()
    expect(rose.color).to_equal("red")
    
def test_violets_are_not_red():
    violet = Violet()
    expect(violet.color).not_to_equal("red")
```
