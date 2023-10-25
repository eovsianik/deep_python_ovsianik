.PHONY: all lint test 

all: test lint

SRC_FILES := .\lruCache.py .\test_lruCache.py

lint:
	flake8 ${SRC_FILES} --max-line-length=100
	pylint ${SRC_FILES} -d C,R


test: $(TEXT_FILES)
	pytest -q --cov=.