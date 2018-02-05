build:
	@echo "Django Console Building Started!"
	python setup.py check
	python setup.py sdist

test:
	@echo "Removing recent buildings..."
	rm -rf djconsole.egg-info/
	rm -rf dist/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	pip uninstall djconsole
	pip install dist/djconsole-0.0.11.tar.gz

upload:
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	@echo "Uploading built package..."
	python setup.py sdist upload

docs: docs/
	@echo "Building documents..."
	mkdocs build

clean:
	@echo "Cleaning..."
	rm -rf site/
	rm -rf djconsole.egg-info/
	rm -rf dist/
