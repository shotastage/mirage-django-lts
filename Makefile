build_all:
	@echo "Django Mirage Building Started!"
	pip install --upgrade pip setuptools wheel
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
	rm -rf mirage_django_lts.egg-info/
	rm -rf dist/
	rm -rf testing/

pyclean:
	find ./mirage -name '*.pyc' -delete -not -path './mirage/scaffold/static/'

rebuild:
	@echo "Removing recent buildings..."
	rm -rf dist/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	pip uninstall mirage-django-lts
	pip install dist/mirage-django-lts-0.2.7.tar.gz

export-requirements:
	pipenv lock -r > requirements.txt
