# Project template for fabric8-analytics projects
#
# 2017, fabric8-analytics developers
#

TEMPFILE := $(shell mktemp -u)
NAME=f8a

.PHONY: install clean venv check coala pylint pydocstyle pytest

install:
	pip3 install -r requirements.txt
	python3 setup.py install

devenv:
	pip3 install -r dev_requirements.txt

venv:
	virtualenv -p python3 venv && source venv/bin/activate && pip3 install -r requirements.txt
	@echo "Run 'source venv/bin/activate' to enter virtual environment and 'deactivate' to return from it"

clean:
	find . -name '*.pyc' -or -name '__pycache__' -print0 | xargs -0 rm -rf
	rm -rf venv venv-coala
	rm -rf dist ${NAME}.egg-info build

pylint:
	@echo ">>> Running pylint"
	pylint ${NAME}

coala:
	echo ">>> Preparing virtual environment for coala" &&\
	  # setuptools is pinned due to dependency conflict &&\
	  [ -d venv-coala ] || virtualenv -p python3 venv-coala && . venv-coala/bin/activate && pip3 install coala-bears "setuptools>=17.0" &&\
	  echo ">>> Running coala" &&\
	  venv-coala/bin/python3 venv-coala/bin/coala --non-interactive

pydocstyle:
	@echo ">>> Running pydocstyle"
	pydocstyle ${NAME}

# Useful aliases
check: pylint pydocstyle coala
test: check

