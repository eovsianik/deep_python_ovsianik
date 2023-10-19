from custom import CustomMeta
import pytest


class ExampleCustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, value=99):
        self.value = value

    def longline(self):
        self.textline = "qwerty"
        return 100

    def __str__(self):
        return "Magic method"

    @classmethod
    def newline(cls):
        return 100


def test_classvalue():
    assert ExampleCustomClass.custom_x == 50
    assert ExampleCustomClass.custom_newline()


def test_old_classvalue_1():
    with pytest.raises(AttributeError):
        ExampleCustomClass.x == 50


def test_old_classvalue_2():
    with pytest.raises(AttributeError):
        ExampleCustomClass.newline()


def test_old_instancevalue_1():
    instance_old = ExampleCustomClass()
    with pytest.raises(AttributeError):
        instance_old.x == 50


def test_old_instancevalue_2():
    instance_old = ExampleCustomClass()
    with pytest.raises(AttributeError):
        instance_old.value == 99


def test_old_instancevalue_3():
    instance_old = ExampleCustomClass()
    with pytest.raises(AttributeError):
        instance_old.longline()


def test_old_instancevalue_4():
    instance_old = ExampleCustomClass()
    with pytest.raises(AttributeError):
        instance_old.textline == "qwerty"


def test_class_instance():
    instance = ExampleCustomClass()
    assert instance.custom_x == 50
    assert instance.custom_value == 99
    assert instance.custom_longline() == 100
    assert instance.custom_textline == "qwerty"


def test_class_instance_magic():
    instance_new = ExampleCustomClass()
    assert str(instance_new) == "Magic method"


def test_instance_dynamic():
    instance_dynamic = ExampleCustomClass()
    instance_dynamic.dynamic = "Dynamic"
    assert instance_dynamic.custom_dynamic == "Dynamic"
    with pytest.raises(AttributeError):
        instance_dynamic.dynamic
