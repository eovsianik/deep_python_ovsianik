from allclasses import (
    MyInt,
    MySlottedClass,
    MyWeakRefClass,
    MyClass,
)

import time


def all_simple(m):
    start_time_simple = time.time()

    objs_simple = [MyClass(i, i + 1) for i in range(m)]

    end_time_simple = time.time()
    creation_time_simple = end_time_simple - start_time_simple
    print(
        "Время создания пачки экземпляров класса с обычными атрибутами:",
        creation_time_simple,
    )

    start_time_simple_change = time.time()

    for obj in objs_simple:
        attr1 = obj.attr1
        obj.attr2 = attr1 + 1

    end_time_simple_change = time.time()
    access_time_simple_change = end_time_simple_change - start_time_simple_change
    print(
        "Время чтения и изменения атрибутов класса с обычными атрибутами:",
        access_time_simple_change,
    )


def all_slots(m):
    start_time_slots = time.time()

    objs_slots = [MySlottedClass(i, i + 1) for i in range(m)]

    end_time_slots = time.time()
    creation_time_slots = end_time_slots - start_time_slots
    print("Время создания пачки экземпляров класса со слотами:", creation_time_slots)

    start_time_slots_change = time.time()

    for obj in objs_slots:
        attr1 = obj.attr1
        obj.attr2 = attr1 + 1

    end_time_slots_change = time.time()
    access_time_slots_change = end_time_slots_change - start_time_slots_change
    print(
        "Время чтения и изменения атрибутов класса со слотами:",
        access_time_slots_change,
    )


def all_weakref(m):
    start_time_weakref = time.time()

    objs_weakref = [MyWeakRefClass(MyInt(i), MyInt(i + 1)) for i in range(m)]

    end_time_weakref = time.time()
    creation_time_weakref = end_time_weakref - start_time_weakref
    print(
        "Время создания пачки экземпляров класса с атрибутами weakref:",
        creation_time_weakref,
    )

    start_time_weakref_change = time.time()

    for obj in objs_weakref:
        attr1 = obj.attr1()
        if attr1 is not None:
            obj.attr2 = attr1 + MyInt(1)

    end_time_weakref_change = time.time()
    access_time_weakref_change = end_time_weakref_change - start_time_weakref_change
    print(
        "Время чтения и изменения атрибутов класса с атрибутами weakref:",
        access_time_weakref_change,
    )


if __name__ == "__main__":
    M = 20000
    all_simple(M)
    all_slots(M)
    all_weakref(M)
