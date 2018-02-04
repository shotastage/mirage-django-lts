build:
	@echo "Removing old packges..."
	rm -rf djconsole.egg-info/
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
	@echo "Removing recent buildings..."
	rm -rf djconsole.egg-info/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	@echo "Uploading built package..."
	python setup.py sdist upload
