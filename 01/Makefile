.PHONY: all lint test 

all: test lint

SRC_FILES := .\score_predict.py .\searching_lines.py .\test_predict.py .\test_searching_lines.py .\testfiles_creation.py

TEXT_FILES := file_or_str.txt test_one_line_sucsess.txt empty_file.txt everywhere_test.txt empty_middle.txt empty_first.txt empty_last.txt capitalfile.txt capital_file_1.txt similar_file.txt last_file.txt

$(TEXT_FILES):
		python testfiles_creation.py

lint:
	flake8 ${SRC_FILES} --max-line-length=100
	pylint ${SRC_FILES} -d C,R

test: $(TEXT_FILES)
	pytest -q --cov=.