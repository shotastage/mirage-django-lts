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
