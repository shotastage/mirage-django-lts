before:
	@echo "Installing reqiorements..."
	pip install pipenv
	pipenv install
	yarn install

build:
	@echo "Building scaffold Sass..."
	./node_module
	@echo "Django Console Building Started!"
	python setup.py check
	python setup.py sdist

upload:
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	@echo "Uploading built package..."
	python setup.py sdist upload

doc: docs/
	@echo "Building documents..."
	mkdocs build

clean:
	@echo "Cleaning..."
	rm -rf site/
	rm -rf djconsole.egg-info/
	rm -rf dist/

test:
	@echo "Removing recent buildings..."
	rm -rf djconsole.egg-info/
	rm -rf dist/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	pip uninstall djconsole
	pip install dist/djconsole-0.0.11.tar.gz

fetch:
	@echo "Fetching assets..."
	curl -O https://raw.githubusercontent.com/jgthms/bulma/master/css/bulma.css
	mv bulma.css ./djconsole/scaffold/static/scss/third-party/_bulma.scss
