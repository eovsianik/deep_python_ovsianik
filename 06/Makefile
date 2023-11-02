.PHONY: all lint test 

all: test lint

SRC_FILES := .\client.py .\test_client.py .\masterserver.py

lint:
	flake8 ${SRC_FILES} --max-line-length=100
	pylint ${SRC_FILES} -d C,R


test: $(TEXT_FILES)
	pytest -q --cov=.