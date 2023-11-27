.PHONY: all lint test 

all: test lint

SRC_FILES := .\lru_cache.py .\test_lrucache.py

lint:
	flake8 ${SRC_FILES} --max-line-length=100
	pylint ${SRC_FILES} -d C,R


test: $(TEXT_FILES)
	pytest -q --cov=.