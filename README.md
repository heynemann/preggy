preggy
======

[![Build Status](https://travis-ci.org/heynemann/preggy.png?branch=master)](https://travis-ci.org/heynemann/preggy)
[![PyPi version](https://pypip.in/v/preggy/badge.png)](https://crate.io/packages/preggy/)
[![PyPi downloads](https://pypip.in/d/preggy/badge.png)](https://crate.io/packages/preggy/)
[![Coverage Status](https://coveralls.io/repos/heynemann/preggy/badge.png?branch=master)](https://coveralls.io/r/heynemann/preggy?branch=master)

**preggy is an assertion library for Python.** What were you `expect`ing?

Extracted from the [PyVows](http://pyvows.org) project.


Installing
==========

Just use `pip` to install preggy:

    pip install preggy


Usage
=====

Simply tell your test what to `expect()`:

```python
from preggy import expect

def test_roses_are_red():
    rose = Rose()
    expect(rose.color).to_equal('red')
    
def test_violets_are_not_red():
    violet = Violet()
    expect(violet.color).not_to_equal('red')
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


Comparison
--------

```python
expect(4).to_be_lesser_than(5)
expect(5).to_be_greater_than(4)
expect(5).Not.to_be_lesser_than(4)
expect(4).not_to_be_greater(5)  # same as previous

expect(4).to_be_lesser_or_equal_to(5)
expect(4).to_be_lesser_or_equal_to(4)
expect(5).not_to_be_lesser_or_equal_to(4)

expect(5).to_be_greater_or_equal_to(4)
expect(5).to_be_greater_or_equal_to(5)
expect(4).not_to_be_greater_or_equal_to(5)

expect("b").to_be_greater_than("a")
expect("a").to_be_lesser_than("b")

expect([1, 2, 3]).to_be_greater_than([1, 2])  # comparing using length
expect((1, 2, 3)).to_be_greater_than((1, 2))  # comparing using length
expect({ "a": "b", "c": "d" }).to_be_greater_than({ "a": "b" })  # comparing using length of keys
```


Similarity
----------

```python
expect('sOmE RandOm     CAse StRiNG').to_be_like('some random case string')

expect(1).to_be_like(1)
expect(1).to_be_like(1.0)
expect(1).to_be_like(long(1))

expect([1, 2, 3]).to_be_like([3, 2, 1])
expect([1, 2, 3]).to_be_like((3, 2, 1))
expect([[1, 2], [3,4]]).to_be_like([4, 3], [2, 1]])

expect({ 'some': 1, 'key': 2 }).to_be_like({ 'key': 2, 'some': 1 })

expect('sOmE RandOm     CAse StRiNG').Not.to_be_like('other string')
expect('sOmE RandOm     CAse StRiNG').not_to_be_like('other string')  # same as previous

expect(1).not_to_be_like(2)
expect([[1, 2], [3,4]]).not_to_be_like([4, 4], [2, 1]])
expect({ 'some': 1, 'key': 2 }).not_to_be_like({ 'key': 3, 'some': 4 })
```


Type
----

```python
expect(os.path).to_be_a_function()
expect(1).to_be_numeric()

expect('some').Not.to_be_a_function()
expect('some').Not.to_be_numeric()
```


True / False
------------

```python
expect(True).to_be_true()
expect('some').to_be_true()
expect([1, 2, 3]).to_be_true()
expect({ 'a': 'b' }).to_be_true()
expect(1).to_be_true()

expect(False).to_be_false()  # not_to_be_true() would work, too. but, it's so...eww
expect(None).to_be_false()
expect('').to_be_false()
expect(0).to_be_false()
expect([]).to_be_false()
expect({}).to_be_false()
```


None
----

```python
expect(None).to_be_null()
expect('some').Not.to_be_null()
expect('some').not_to_be_null()  # same as previous
```


Inclusion
---------

```python
expect([1, 2, 3]).to_include(2)
expect((1, 2, 3)).to_include(2)
expect('123').to_include('2')
expect({ 'a': 1, 'b': 2, 'c': 3}).to_include('b')

expect([1, 3]).Not.to_include(2)  # or, exclusion...
```


Regular Expressions
-------------------

```python
expect('some').to_match(r'^[a-z]+')
expect('Some').Not.to_match(r'^[a-z]+')
```


Length
------

```python
expect([1, 2, 3]).to_length(3)
expect((1, 2, 3)).to_length(3)
expect('abc').to_length(3)
expect({ 'a': 1, 'b': 2, 'c': 3}).to_length(3)
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
expect('').to_be_empty()

expect([1]).not_to_be_empty()
expect((1,2)).not_to_be_empty()
expect({'a': 1}).not_to_be_empty()
expect('roses are red').not_to_be_empty()
```


Exceptions
----------

```python
expect(RuntimeError()).to_be_an_error() 
expect(RuntimeError()).to_be_an_error_like(RuntimeError)
expect(ValueError('error')).to_have_an_error_message_of('error')

expect("I'm not an error").Not.to_be_an_error()
expect(ValueError()).Not.to_be_an_error_like(RuntimeError)
expect(ValueError('some')).Not.to_have_an_error_message_of('error')
```


Development
===========

Hacking `preggy` is simple.

- Code whatever you feel like
- Test your changes
- Check the tests on preggy’s supported version of Python: 2.6, 2.7, 3.2, 3.3, and pypy.

For that last item, we recommend `pythonbrew` to install all those Python versions. 


Installing `pythonbrew`
-----------------------

**Step 1:** Grab the file and install it:

```bash
    $ curl -kL http://xrl.us/pythonbrewinstall | bash
```

**Step 2:** Add this line to your `.bashrc` or `.bash_profile` (or your favorite shell’s equivalent):

```bash
    [[ -s $HOME/.pythonbrew/etc/bashrc ]] && source $HOME/.pythonbrew/etc/bashrc
```

**Step 3:** Install supported Python versions (*except pypy*; see below!):

```bash
# find out the available versions
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

# install the supported versions of Python
$ pythonbrew install Python-2.6.8
$ pythonbrew install Python-2.7.3
$ pythonbrew install Python-3.2.3
$ pythonbrew install Python-3.3.0
```

### Pypy

Pypy should be installed separately:

- [pypy download page](http://pypy.org/download.html)
- Or, if you use OS X and Homebrew: `brew install pypy`


Now you're ready to build.
--------------------------
To build preggy for all supported Python versions:

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
