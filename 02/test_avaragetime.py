import time

from avaragetime import mean


def test_no_call():
    @mean(3)
    def foo():
        time.sleep(0.5)

    number_of_calls = len(foo.__closure__[2].cell_contents)
    assert number_of_calls == 0


def test_several_calls():
    @mean(3)
    def foo():
        time.sleep(0.5)

    for _ in range(10):
        foo()

    number_of_calls = len(foo.__closure__[2].cell_contents)
    assert number_of_calls == 3


def test_less_calls():
    @mean(3)
    def foo():
        time.sleep(0.5)

    foo()

    number_of_calls = len(foo.__closure__[2].cell_contents)
    assert number_of_calls == 1


def test_result():
    @mean(5)
    def foo():
        time.sleep(0.5)

    for _ in range(10):
        foo()

    meantime = sum(foo.__closure__[2].cell_contents) / len(
        foo.__closure__[2].cell_contents
    )
    assert 0.49 < meantime < 0.51


def test_another_result():
    @mean(5)
    def foo():
        time.sleep(1)

    for _ in range(10):
        foo()

    meantime = sum(foo.__closure__[2].cell_contents) / len(
        foo.__closure__[2].cell_contents
    )
    assert 0.99 < meantime < 1.1
