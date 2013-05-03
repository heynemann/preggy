test:
	@nosetests -vv --with-yanc -s --with-coverage --cover-erase --cover-inclusive --cover-package=preggy tests/

ci-test:
	@nosetests -vv --with-yanc -s --with-coverage --cover-erase --cover-inclusive --cover-package=preggy tests/

tox:
	# refer to the readme for instructions on installing these python versions to run tox
	@PATH=$$PATH:~/.pythonbrew/pythons/Python-2.6.*/bin/:~/.pythonbrew/pythons/Python-2.7.*/bin/:~/.pythonbrew/pythons/Python-3.2.3/bin/:~/.pythonbrew/pythons/Python-3.3.0/bin/ tox

setup:
	@pip install -e .[tests]
