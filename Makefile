all: build

build:
	python3 setup.py sdist bdist_wheel

test-publish: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish: clean build
	twine upload dist/*

clean:
	rm -rf build dist *.egg-info

.PHONY: build publish test-publish clean
