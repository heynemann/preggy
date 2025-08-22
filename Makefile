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
