.PHONY: all install test

PYTHON_BIN ?= python
ACT_DIR ?= ./.venv/bin

all: init install test

init:
	$(PYTHON_BIN) -m venv .venv
	$(ACT_DIR)/pip install -r requirements.txt

build:
	$(ACT_DIR)/python setup.py build

install:
	$(ACT_DIR)/python setup.py install

test: install
	$(ACT_DIR)/pytest tests

