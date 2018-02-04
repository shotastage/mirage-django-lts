build:
	@echo "Django Console Building Started!"
	python setup.py check
	python setup.py sdist

update:
	@echo "Removing recent buildings..."
	rm -rf djconsole.egg-info/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist

upload:
	@echo "Removing recent buildings..."
	rm -rf djconsole.egg-info/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	@echo "Uploading built package..."
	python setup.py sdist upload
