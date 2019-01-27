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
	@echo "Django Mirage Building Started!"
	python setup.py check
	python setup.py sdist


upload:
	@echo "Building Django Mirage..."
	python setup.py check
	python setup.py bdist_wheel

	@echo "Uploading built package..."
	twine upload dist/*

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

rebuild:
	@echo "Removing recent buildings..."
	rm -rf dist/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	pip uninstall django-mirage
	pip install dist/django-mirage-0.1.7.tar.gz

export-requirements:
	pipenv lock -r > requirements.txt
