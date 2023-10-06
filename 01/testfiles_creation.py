def file_creation():
    """
    Создание текстовых файлов для тестирования генератора search_lines
    """
    # Для тестов test_file_not_str,
    file_not_str = open("file_or_str.txt", "w", encoding="utf-8")
    file_not_str.write("word1 word2 word3")
    file_not_str.close()

    # Для тестов test_one_line_sucsess_and_not, test_empty_list
    test_one_line_sucsess = open("test_one_line_sucsess.txt", "w", encoding="utf-8")
    test_one_line_sucsess.write("word1 word2 word3")
    test_one_line_sucsess.close()

    # Для тестов test_empty_file, test_everything_is_empty
    empty_file = open("empty_file.txt", "w", encoding="utf-8")
    empty_file.close()

    # Для тестов test_it_is_everywhere
    everywhere_test = open("everywhere_test.txt", "w", encoding="utf-8")
    everywhere_test.writelines(
        [
            "The apple is red\n",
            "I ate an apple for breakfast\n",
            "My favorite fruit is the apple\n",
            "An apple a day keeps the doctor away\n",
            "The apple tree in our backyard is full of fruit\n",
        ]
    )
    everywhere_test.close()

    # Для тестов test_empty_line
    empty_mid = open("empty_middle.txt", "w", encoding="utf-8")
    empty_mid.writelines(
        [
            "The apple is red\n",
            "\n",
            "The apple tree in our backyard is full of fruit\n",
        ]
    )
    empty_mid.close()

    # Для тестов test_empty_line
    empty_first = open("empty_first.txt", "w", encoding="utf-8")
    empty_first.writelines(
        [
            "\n",
            "The apple is red\n",
            "The apple tree in our backyard is full of fruit\n",
        ]
    )
    empty_first.close()

    # Для тестов test_empty_line
    empty_first = open("empty_last.txt", "w", encoding="utf-8")
    empty_first.writelines(
        [
            "The apple is red\n",
            "The apple tree in our backyard is full of fruit\n",
            "\n",
        ]
    )
    empty_first.close()

    # Для тестов capital
    capital_file = open("capital_file_.txt", "w", encoding="utf-8")
    capital_file.writelines(
        [
            "BLUEBERRIES are incredibly healthy and nutritious\n",
            "They are packed with antioxidants which help protect the body against free radicals\n",
            "In addition to their health benefits BLUEBERRIES are also delicious and versatile\n",
            "You can enjoy them fresh add them to smoothies or use them in baking\n",
        ]
    )
    capital_file.close()

    capital_file = open("capital_file_1.txt", "w", encoding="utf-8")
    capital_file.writelines(
        [
            "BLUEBERRIES are incredibly healthy AND nutritious\n",
            "They are packed with antioxidants which help protect the body against free radicals\n",
            "In addition to their health benefits blueberries are also delicious and versatile\n",
            "You can enjoy them fresh add them to smoothies or use them in baking\n",
        ]
    )
    capital_file.close()

    similar_file = open("similar_file.txt", "w", encoding="utf-8")
    similar_file.writelines(
        [
            "rose and blue\n",
            "roses and blueberries\n",
            "straw roof\n",
            "strawberry is tasty\n",
        ]
    )
    similar_file.close()

    all_str = open("last_file.txt", "w", encoding="utf-8")
    all_str.writelines(
        [
            "rose and blue\n",
            "string_give_all_string\n",
            "roses and blueberries\n",
            "straw roof\n",
            "strawberry is tasty\n",
        ]
    )
    all_str.close()


file_creation()
