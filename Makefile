NOSE_TEST_COVER_OPTS = --with-coverage --cover-erase --cover-inclusive --cover-package=preggy --cover-package=preggy.assertions --cover-package=preggy.assertions.types
NOSE_TEST = @nosetests -vv --detailed-errors --with-yanc -s $(NOSE_TEST_COVER_OPTS) tests/

test:
	$(NOSE_TEST)

ci-test:
	$(NOSE_TEST)

tox:
	# refer to the readme for instructions on installing these python versions to run tox
	@PATH=$$PATH:~/.pythonbrew/pythons/Python-2.6.*/bin/:~/.pythonbrew/pythons/Python-2.7.*/bin/:~/.pythonbrew/pythons/Python-3.2.3/bin/:~/.pythonbrew/pythons/Python-3.3.0/bin/ tox

setup:
	@pip install -e .[tests]
