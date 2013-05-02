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
expect(5).not_to_equal(4)  # same as previous
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
expect("sOmE RandOm     CAse StRiNG").not_to_be_like('other string')  # same as previous

expect(1).not_to_be_like(2)
expect([[1, 2], [3,4]]).not_to_be_like([4, 4], [2, 1]])
expect({ 'some': 1, 'key': 2 }).not_to_be_like({ 'key': 3, 'some': 4 })
```

Type
----
```python
expect(os.path).to_be_a_function()
expect(1).to_be_numeric()

expect("some").Not.to_be_a_function()
expect("some").Not.to_be_numeric()
```

Truth
-----

```python
expect(True).to_be_true()
expect("some").to_be_true()
expect([1, 2, 3]).to_be_true()
expect({ "a": "b" }).to_be_true()
expect(1).to_be_true()

# while not_to_be_true would work as well, it's just ugly, right?
expect(False).to_be_false()
expect(None).to_be_false()
expect("").to_be_false()
expect(0).to_be_false()
expect([]).to_be_false()
expect({}).to_be_false()
```

None
----

```python
expect(None).to_be_null()
expect("some").Not.to_be_null()
expect("some").not_to_be_null()  # same as previous
```

Inclusion
---------

```python
expect([1, 2, 3]).to_include(2)
expect((1, 2, 3)).to_include(2)
expect("123").to_include("2")
expect({ "a": 1, "b": 2, "c": 3}).to_include("b")

expect([1, 3]).Not.to_include(2)
```

Regular Expressions
-------------------

```python
expect('some').to_match(r'^[a-z]+')

expect("Some").Not.to_match(r'^[a-z]+')
```

Length
------

```python
expect([1, 2, 3]).to_length(3)
expect((1, 2, 3)).to_length(3)
expect("abc").to_length(3)
expect({ "a": 1, "b": 2, "c": 3}).to_length(3)
expect(lifo_queue).to_length(2)
expect(queue).to_length(3)

expect([1]).Not.to_length(3)
expect([1]).not_to_length(3)  # same as previous
```

Emptiness
---------

```python
expect([]).to_be_empty()
expect(tuple()).to_be_empty()
expect({}).to_be_empty()
expect("").to_be_empty()

expect([1]).not_to_be_empty()
expect((1,2)).not_to_be_empty()
expect({"a": 1}).not_to_be_empty()
expect("roses are red").not_to_be_empty()
```

Exceptions
----------

```python
expect(RuntimeError()).to_be_an_error() 
expect(RuntimeError()).to_be_an_error_like(RuntimeError)
expect(ValueError("error")).to_have_an_error_message_of("error")

expect("I'm not an error").Not.to_be_an_error()
expect(ValueError()).Not.to_be_an_error_like(RuntimeError)
expect(ValueError("some")).Not.to_have_an_error_message_of("error")
```
