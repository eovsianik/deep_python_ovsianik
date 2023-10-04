from unittest.mock import Mock
from unittest import mock
import pytest
import json

from findwords import parse_json


def test_return_twocallback():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["key1", "key2"],
        ["word1", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("key1", "Word1"),
        mock.call("key2", "word3"),
    ]


def test_required_fields_is_none():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        None,
        ["word1", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("key1", "Word1"),
        mock.call("key2", "word3"),
    ]


def test_keywords_is_none():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["key1", "key3"],
        None,
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("key1", "Word1"),
        mock.call("key1", "word2"),
    ]


def test_keywords_and_required_fields_are_none():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        None,
        None,
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("key1", "Word1"),
        mock.call("key1", "word2"),
        mock.call("key2", "word2"),
        mock.call("key2", "word3"),
    ]


def test_all():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["key1", "key2"],
        ["word1", "word2", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("key1", "Word1"),
        mock.call("key1", "word2"),
        mock.call("key2", "word2"),
        mock.call("key2", "word3"),
    ]


def test_not_found_because_keys():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["key3", "key4"],
        ["word1", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_count == 0


def test_not_found_because_words():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["key1", "key2"],
        ["word5", "word6"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_count == 0


def test_capital_required_fields():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["KEY1", "key2"],
        ["word1", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [mock.call("key2", "word3")]


def test_capital_keywords():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["key1", "key2"],
        ["WORD2", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("key1", "word2"),
        mock.call("key2", "word2"),
        mock.call("key2", "word3"),
    ]


def test_keywords_and_required_fields_are_capital():
    keyword_callback_mock = Mock()

    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["KEY1", "key2"],
        ["WORD2", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("key2", "word2"),
        mock.call("key2", "word3"),
    ]


def test_json_capital_keys():
    keyword_callback_mock = Mock()

    parse_json(
        '{"KEY1": "Word1 word2", "KEY2": "word2 word3"}',
        ["key1", "key2"],
        ["WORD2", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_count == 0


def test_json_capital_keys_and_words_not_found():
    keyword_callback_mock = Mock()

    parse_json(
        '{"KEY1": "WORD1 word2", "KEY2": "word2 word3"}',
        ["key1", "key2"],
        ["WORD2", "word3"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_count == 0


def test_json_capital_keys_and_words():
    keyword_callback_mock = Mock()

    parse_json(
        '{"KEY1": "WORD1 word2", "KEY2": "word2 word3"}',
        ["KEY1", "key2"],
        ["WORD2", "word1"],
        keyword_callback_mock,
    )

    assert keyword_callback_mock.call_args_list == [
        mock.call("KEY1", "word2"),
        mock.call("KEY1", "WORD1"),
    ]


def test_wrong_json():
    keyword_callback_mock = Mock()

    with pytest.raises(json.decoder.JSONDecodeError):
        parse_json(
            '{"KEY1" = "WORD1 word2", "KEY2": "word2 word3"}',
            ["KEY1", "key2"],
            ["WORD2", "word1"],
            keyword_callback_mock,
        )
