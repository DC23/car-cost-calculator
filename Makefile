SHELL=/bin/sh
PACKAGE_NAME=car_cost_calculator

.SILENT:
.IGNORE:

.PHONY: help
help:
	echo
	echo 'Utility Makefile for Car Cost Calculator'
	echo '============================'
	echo
	echo 'Targets supported are:'
	echo
	echo '  * clean: removes the build directories, as well as __pycache__ and *.pyc files. Note that a clean also removes the generated documentation (as this is placed into build/docs).'
	echo '  * test: runs py.test.'
	echo '  * lint: runs pylint.'

.PHONY: test
test:
	py.test

.PHONY: clean
clean:
	echo Cleaning ...
	rm -rf build/
	find ./$(PACKAGE_NAME)/ -name "__pycache__" -exec rm -rf {} \;
	find ./$(PACKAGE_NAME)/ -name "*.pyc" -exec rm -rf {} \;
	echo ... done

.PHONY: lint
lint:
	pylint ./$(PACKAGE_NAME)/
