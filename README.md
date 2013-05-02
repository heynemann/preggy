preggy
======

[![Build Status](https://travis-ci.org/heynemann/preggy.png?branch=master)](https://travis-ci.org/heynemann/preggy)

preggy is a collection of expectations for python applications, extracted from the pyVows project.

Installing
==========

Just use `pip` to install preggy:

    pip install preggy

Usage
=====

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

Built-in Expectations
=====================

Equality
--------

```python
expect(4).to_equal(4)
expect(5).Not.to_equal(4)
```

Similarity
----------

```python
expect("sOmE RandOm     CAse StRiNG").to_be_like('some random case string')

expect(1).to_be_like(1)
expect(1).to_be_like(1.0)
expect(1).to_be_like(long(1))

expect([1, 2, 3]).to_be_like([3, 2, 1])
expect([1, 2, 3]).to_be_like((3, 2, 1))
expect([[1, 2], [3,4]]).to_be_like([4, 3], [2, 1]])

expect({ 'some': 1, 'key': 2 }).to_be_like({ 'key': 2, 'some': 1 })

expect("sOmE RandOm     CAse StRiNG").Not.to_be_like('other string')
expect(1).Not_to_be_like(2)
expect([[1, 2], [3,4]]).Not.to_be_like([4, 4], [2, 1]])
expect({ 'some': 1, 'key': 2 }).Not.to_be_like({ 'key': 3, 'some': 4 })
```
