.PHONY: all lint 

all: lint

SRC_FILES := .\profiledeco.py .\test_profiledeco.py .\allclasses.py .\timemeasure.py .\profilemeasure.py

lint:
	flake8 ${SRC_FILES} --max-line-length=100
	pylint ${SRC_FILES} -d C,R
