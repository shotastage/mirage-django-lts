before_all:
	@echo "WARNING: BT"
	@echo "Installing reqiorements..."
	pip install pipenv
	pipenv install
	yarn install

before_node:
	@echo "Installing node requirements..."
	yarn install

build_all:
	@echo "Building scaffold Sass..."
	./node_modules/.bin/node-sass ./djconsole/scaffold/static/scss/main.scss djconsole/scaffold/static/style/main.css
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
	rm -rf node_modules/
	rm -rf testing/

test:
	@echo "Removing recent buildings..."
	rm -rf dist/
	@echo "Building scaffold Sass..."
	./node_modules/.bin/node-sass ./djconsole/scaffold/static/scss/main.scss djconsole/scaffold/static/style/main.css
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	pip uninstall djconsole
	pip install dist/djconsole-0.0.11.tar.gz

fetch:
	@echo "Fetching assets..."
	curl -O https://raw.githubusercontent.com/jgthms/bulma/master/css/bulma.css
	mv bulma.css ./djconsole/scaffold/static/scss/third-party/_bulma.scss
