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
	echo '  * develop: installs car-cost-calculator in development mode.'
	echo '  * uninstall: removes the development package from pip.'
	echo '  * test: runs py.test.'
	echo '  * lint: runs pylint.'
	echo '  * sdist: builds a source distribution.'
	echo '  * upload: upload builds to PyPI.'

.PHONY: test
test:
	py.test

.PHONY: clean
clean:
	echo Cleaning ...
	rm -rf build/
	rm -rf .ipynb_checkpoints/
	rm -rf .pytest_cache/
	find ./$(PACKAGE_NAME)/ -name "__pycache__" -exec rm -rf {} \;
	find ./$(PACKAGE_NAME)/ -name "*.pyc" -exec rm -rf {} \;
	echo ... done

.PHONY: install-deps
install-deps:
	pip install -e.[dev,test]

.PHONY: develop
develop: install-deps
	python setup.py develop

.PHONY: uninstall
uninstall:
	pip uninstall --yes $(PACKAGE_NAME)
	rm -rf *.egg-info/

.PHONY: lint
lint:
	pylint ./$(PACKAGE_NAME)/

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: bdist_wheel
bdist_wheel:
	python setup.py bdist_wheel

# Upload package to PyPI. You must edit this if you only require specific package types.
# .PHONY: upload
# upload: clean
# 	rm -rf dist/
# 	python setup.py sdist bdist_wheel
# 	twine upload dist/*

