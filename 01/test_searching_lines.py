from searching_lines import search_lines


def test_file_not_str():
    my_test_file = open("file_or_str.txt", "r", encoding="utf-8")
    comparison = [line for line in search_lines(my_test_file, ["word3"])]
    my_test_file.close()
    assert comparison == ["word1 word2 word3"]


def test_str_not_file():
    comparison = [line for line in search_lines("file_or_str.txt", ["word2"])]
    assert comparison == ["word1 word2 word3"]


def test_one_line_sucsess_and_not():
    comparison_sucsess = [
        line for line in search_lines("test_one_line_sucsess.txt", ["word1"])
    ]
    assert comparison_sucsess == ["word1 word2 word3"]

    comparison_unsucsess = [
        line for line in search_lines("test_one_line_sucsess.txt", ["word4"])
    ]
    assert comparison_unsucsess == []


def test_empty_file():
    comparison = [line for line in search_lines("empty_file.txt", ["word1"])]
    assert comparison == []


def test_empty_list():
    comparison = [line for line in search_lines("test_one_line_sucsess.txt", [])]
    assert comparison == []


def test_everything_is_empty():
    comparison = [line for line in search_lines("empty_file.txt", [])]
    assert comparison == []


def test_it_is_everywhere():
    comparison = [line for line in search_lines("everywhere_test.txt", ["apple"])]
    assert comparison == [
        "The apple is red\n",
        "I ate an apple for breakfast\n",
        "My favorite fruit is the apple\n",
        "An apple a day keeps the doctor away\n",
        "The apple tree in our backyard is full of fruit\n",
    ]


def test_give_too_return_one():
    comparison = [
        line for line in search_lines("test_one_line_sucsess.txt", ["word1", "word2"])
    ]
    assert comparison == ["word1 word2 word3"]


def test_empty_line_middle_word_before():
    comparison = [line for line in search_lines("empty_middle.txt", ["red"])]
    assert comparison == ["The apple is red\n"]


def test_empty_line_middle_word_before_and_after():
    comparison = [line for line in search_lines("empty_middle.txt", ["The"])]
    assert comparison == [
        "The apple is red\n",
        "The apple tree in our backyard is full of fruit\n",
    ]


def test_empty_line_middle_word_after():
    comparison = [line for line in search_lines("empty_middle.txt", ["backyard"])]
    assert comparison == ["The apple tree in our backyard is full of fruit\n"]


def test_empty_line_middle_not_word():
    comparison = [line for line in search_lines("empty_middle.txt", ["blue"])]
    assert comparison == []


def test_empty_line_middle_empty_wordlist():
    comparison = [line for line in search_lines("empty_middle.txt", [])]
    assert comparison == []


def test_empty_line_first_word_after():
    comparison = [line for line in search_lines("empty_first.txt", ["red"])]
    assert comparison == ["The apple is red\n"]


def test_empty_line_first_not_word():
    comparison = [line for line in search_lines("empty_first.txt", ["blue"])]
    assert comparison == []


def test_empty_line_first_empty_wordlist():
    comparison = [line for line in search_lines("empty_first.txt", [])]
    assert comparison == []


def test_empty_line_last_word_before():
    comparison = [line for line in search_lines("empty_last.txt", ["red"])]
    assert comparison == ["The apple is red\n"]


def test_empty_line_last_not_word():
    comparison = [line for line in search_lines("empty_last.txt", ["blue"])]
    assert comparison == []


def test_empty_line_last_empty_wordlist():
    comparison = [line for line in search_lines("empty_last.txt", [])]
    assert comparison == []


def test_capital_letter_only_wordlist():
    comparison = [line for line in search_lines("everywhere_test.txt", ["APPLE"])]
    assert comparison == [
        "The apple is red\n",
        "I ate an apple for breakfast\n",
        "My favorite fruit is the apple\n",
        "An apple a day keeps the doctor away\n",
        "The apple tree in our backyard is full of fruit\n",
    ]


def test_capital_letter_only_text():
    comparison = [line for line in search_lines("capital_file_.txt", ["blueberries"])]
    assert comparison == [
        "BLUEBERRIES are incredibly healthy and nutritious\n",
        "In addition to their health benefits BLUEBERRIES are also delicious and versatile\n",
    ]


def test_capital_letter_wordlist_and_text():
    comparison = [
        line for line in search_lines("capital_file_1.txt", ["blueberries", "AND"])
    ]
    assert comparison == [
        "BLUEBERRIES are incredibly healthy AND nutritious\n",
        "In addition to their health benefits blueberries are also delicious and versatile\n",
    ]


def test_almost_similar_wordlist_and_text():
    comparison = [
        line for line in search_lines("similar_file.txt", ["blue", "straw", "rose"])
    ]
    assert comparison == ["rose and blue\n", "straw roof\n"]


def test_string_give_all_string():
    comparison = [
        line for line in search_lines("last_file.txt", ["string_give_all_string"])
    ]
    assert comparison == ["string_give_all_string\n"]
