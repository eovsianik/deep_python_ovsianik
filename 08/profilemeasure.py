from allclasses import (
    MyInt,
    MySlottedClass,
    MyWeakRefClass,
    MyClass,
)

from memory_profiler import profile


@profile
def all_simple(m):
    objs_simple = [MyClass(i, i + 1) for i in range(m)]

    for obj in objs_simple:
        attr1 = obj.attr1
        obj.attr2 = attr1 + 1


@profile
def all_slots(m):
    objs_slots = [MySlottedClass(i, i + 1) for i in range(m)]

    for obj in objs_slots:
        attr1 = obj.attr1
        obj.attr2 = attr1 + 1


@profile
def all_weakref(m):
    objs_weakref = [MyWeakRefClass(MyInt(i), MyInt(i + 1)) for i in range(m)]

    for obj in objs_weakref:
        attr1 = obj.attr1()
        if attr1 is not None:
            obj.attr2 = attr1 + MyInt(1)


if __name__ == "__main__":
    n = 50_000
    all_simple(n)
    all_slots(n)
    all_weakref(n)
