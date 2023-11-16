import weakref


class MyClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class MySlottedClass:
    __slots__ = ["attr1", "attr2"]

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class MyInt:
    def __init__(self, value):
        self.value = int(value)


class MyWeakRefClass:
    def __init__(self, attr1, attr2):
        self.attr1 = weakref.ref(attr1)
        self.attr2 = weakref.ref(attr2)
