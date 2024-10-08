import score_predict


def test_bad_score(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Apple"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.1)

    assert score_predict.predict_message_mood(test_message, test_model) == "неуд"


def test_normal_score(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Orange"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.5)

    assert score_predict.predict_message_mood(test_message, test_model) == "норм"


def test_excellent_score(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Blueberry"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.9)

    assert score_predict.predict_message_mood(test_message, test_model) == "отл"


def test_border_conditions_bad_score(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Strawberry"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.3)

    assert score_predict.predict_message_mood(test_message, test_model) == "норм"


def test_border_conditions_excellent_score(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Melon"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.8)

    assert score_predict.predict_message_mood(test_message, test_model) == "норм"


def test_get_bad_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Watermelon"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.3)

    assert (
        score_predict.predict_message_mood(test_message, test_model, bad_thresholds=0.4)
        == "неуд"
    )


def test_get_good_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Trees"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.8)

    assert (
        score_predict.predict_message_mood(
            test_message, test_model, good_thresholds=0.7
        )
        == "отл"
    )


def test_get_bad_and_good_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Peach"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.3)

    assert (
        score_predict.predict_message_mood(
            test_message, test_model, bad_thresholds=0.2, good_thresholds=0.7
        )
        == "норм"
    )


def test_less_bad_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Cowberry"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.299)

    assert score_predict.predict_message_mood(test_message, test_model) == "неуд"


def test_more_bad_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Cloudberry"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.301)

    assert score_predict.predict_message_mood(test_message, test_model) == "норм"


def test_less_good_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Physalis"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.799)

    assert score_predict.predict_message_mood(test_message, test_model) == "норм"


def test_more_good_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Sunflower"
    mocker.patch("score_predict.SomeModel.predict", return_value=0.801)

    assert score_predict.predict_message_mood(test_message, test_model) == "отл"


def test_mixed_thresholds(mocker):
    test_model = score_predict.SomeModel()
    test_message = "Rose"
    mocker.patch("score_predict.SomeModel.predict", return_value=1.7)

    assert (
        score_predict.predict_message_mood(
            test_message, test_model, bad_thresholds=0.9, good_thresholds=0.2
        )
        == "отл"
    )


def test_is_str_pred(mocker):
    mock_func = mocker.Mock(wraps=lambda *args: 0.5)
    test_model = score_predict.SomeModel()
    test_message = "Sparrow"
    mocker.patch("score_predict.SomeModel.predict", mock_func)
    assert score_predict.predict_message_mood(test_message, test_model) == "норм"
    assert mock_func.call_args_list == [mocker.call(test_message)]
