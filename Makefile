before_all:
	@echo "Installing reqiorements..."
	pip install pipenv
	pipenv install
	yarn install

before_node:
	@echo "Installing node requirements..."
	yarn install

build_all:
	@echo "Building scaffold Sass..."
	./node_modules/.bin/node-sass ./mirage/scaffold/static/scss/main.scss mirage/scaffold/static/style/main.css
	@echo "Django Console Building Started!"
	python setup.py check
	python setup.py sdist


build_node:
	./node_modules/.bin/node-sass ./mirage/scaffold/static/scss/main.scss mirage/scaffold/static/style/main.css


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
	rm -rf django_mirage.egg-info/
	rm -rf dist/
	rm -rf node_modules/
	rm -rf testing/

pyclean:
	find ./mirage -name '*.pyc' -delete -not -path './mirage/scaffold/static/'

test:
	@echo "Removing recent buildings..."
	rm -rf dist/
	@echo "Building scaffold Sass..."
	./node_modules/.bin/node-sass ./mirage/scaffold/static/scss/main.scss mirage/scaffold/static/style/main.css
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	pip uninstall django-mirage
	pip install dist/django-mirage-0.0.24.tar.gz

fetch:
	@echo "Fetching assets..."
	curl -O https://raw.githubusercontent.com/jgthms/bulma/master/css/bulma.css
	curl -O https://raw.githubusercontent.com/jgthms/bulma/master/css/bulma.css.map
	mv bulma.css ./mirage/scaffold/static/scss/third-party/_bulma.scss
	mv bulma.css.map ./mirage/scaffold/static/scss/third-party/bulma.css.map
