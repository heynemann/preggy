Developing
==========

So, you want to contribute?  Awesome!  Hacking `preggy` is simple:

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

