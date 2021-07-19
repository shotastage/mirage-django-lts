build_all:
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
	pipenv uninstall mirage-django-lts
	pipenv install dist/mirage-django-lts-0.2.3.tar.gz

export-requirements:
	pipenv lock -r > requirements.txt
