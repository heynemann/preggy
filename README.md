preggy
======

[![Build Status](https://travis-ci.org/heynemann/preggy.png?branch=master)](https://travis-ci.org/heynemann/preggy) [![codeq](https://codeq.io/github/heynemann/preggy/badges/master.png)](https://codeq.io/github/heynemann/preggy/branches/master)
[![PyPi version](https://pypip.in/v/preggy/badge.png)](https://crate.io/packages/preggy/)
[![PyPi downloads](https://pypip.in/d/preggy/badge.png)](https://crate.io/packages/preggy/)

preggy is a collection of expectations for Python testing, extracted from the [PyVows](http://pyvows.org) project.


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


True / False
------------

```python
expect(True).to_be_true()
expect("some").to_be_true()
expect([1, 2, 3]).to_be_true()
expect({ "a": "b" }).to_be_true()
expect(1).to_be_true()

expect(False).to_be_false()  # not_to_be_true() would work, too. but, it's so...eww
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

expect([1, 3]).Not.to_include(2)  # or, exclusion...
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


Development
===========

Hacking preggy is very simple. Just code whatever you feel like and then make sure it has tests and it runs in all supported python versions: 2.6, 2.7, 3.2, 3.3 and pypy.

We recommend using pythonbrew to install all those python versions to your home, like so:

    $ curl -kL http://xrl.us/pythonbrewinstall | bash

Then add this line to your .bashrc (or .bash_profile):

    [[ -s $HOME/.pythonbrew/etc/bashrc ]] && source $HOME/.pythonbrew/etc/bashrc

After that all you have to do is install all the needed versions of python:

    $ pythonbrew list -k
    Python-1.5.2
    Python-1.6.1
    Python-2.0.1
    Python-2.1.3
    Python-2.2.3
    Python-2.3.7
    Python-2.4.6
    Python-2.5.6
    Python-2.6.8
    Python-2.7.3
    Python-3.0.1
    Python-3.1.4
    Python-3.2.3
    Python-3.3.0

    $ pythonbrew install Python-2.6.8
    $ pythonbrew install Python-2.7.3
    $ pythonbrew install Python-3.2.3
    $ pythonbrew install Python-3.3.0

Pypy should be installed separately. You should check Pypy's own installation instructions.

After having all the python versions in your home directory, running the build for all python version is as simple as:

    make tox


License
=======

The MIT License (MIT)

Copyright (c) 2013 Bernardo Heynemann <heynemann@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
