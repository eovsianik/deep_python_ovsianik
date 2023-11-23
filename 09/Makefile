.PHONY: all lint

all: lint

SRC_FILES := .\logLruCache.py

lint:
	flake8 ${SRC_FILES} --max-line-length=100
	pylint ${SRC_FILES} -d C,R
