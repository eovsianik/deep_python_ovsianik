.PHONY: all lint test 

all: test lint

SRC_FILES := .\custom.py .\test_custom.py .\test_userdescriptor.py .\userdescriptor.py

lint:
	flake8 ${SRC_FILES} --max-line-length=100 --extend-ignore=F841
	pylint ${SRC_FILES} -d C,R,E1101,W0104,W0612,W0201


test: $(TEXT_FILES)
	pytest -q --cov=.