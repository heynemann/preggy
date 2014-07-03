NOSE_TEST_COVER_OPTS = --with-coverage --cover-package=preggy --cover-package=preggy.assertions --cover-package=preggy.assertions.types
NOSE_TEST = @nosetests -vv --detailed-errors --with-yanc -s $(NOSE_TEST_COVER_OPTS) tests/

test:
	$(NOSE_TEST) $(NOSE_TEST_COVER_OPTS)

ci-test:
	@rm -f .coverage
	$(NOSE_TEST) --with-coverage

tox:
	@tox

setup:
	@pip install -e .[tests]

release:
	@git commit -am "Release `python -c "import preggy; print preggy.__version__"`"
	@git push
	@git tag `python -c "import preggy; print preggy.__version__"`
	@git push --tags
	@python setup.py sdist upload
