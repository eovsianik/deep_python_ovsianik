from itertools import zip_longest


class CustomList(list):
    def __add__(self, anotherlist):
        if isinstance(anotherlist, CustomList) or isinstance(anotherlist, list):
            return CustomList(
                a + b for a, b in zip_longest(self, anotherlist, fillvalue=0)
            )

    def __sub__(self, anotherlist):
        if isinstance(anotherlist, CustomList) or isinstance(anotherlist, list):
            return CustomList(
                a - b for a, b in zip_longest(self, anotherlist, fillvalue=0)
            )

    def __radd__(self, anotherlist):
        if isinstance(anotherlist, list):
            return CustomList(
                a + b for a, b in zip_longest(anotherlist, self, fillvalue=0)
            )

    def __rsub__(self, anotherlist):
        if isinstance(anotherlist, list):
            return CustomList(
                a - b for a, b in zip_longest(anotherlist, self, fillvalue=0)
            )

    def __str__(self):
        return f"{super().__str__()}:{sum(self)}"

    def __le__(self, other):
        if isinstance(self, CustomList) and isinstance(other, CustomList):
            return sum(self) <= sum(other)

    def __lt__(self, other):
        if isinstance(self, CustomList) and isinstance(other, CustomList):
            return sum(self) < sum(other)

    def __eq__(self, other):
        if isinstance(self, CustomList) and isinstance(other, CustomList):
            return sum(self) == sum(other)

    def __ne__(self, other):
        if isinstance(self, CustomList) and isinstance(other, CustomList):
            return sum(self) != sum(other)

    def __ge__(self, other):
        if isinstance(self, CustomList) and isinstance(other, CustomList):
            return sum(self) >= sum(other)

    def __gt__(self, other):
        if isinstance(self, CustomList) and isinstance(other, CustomList):
            return sum(self) > sum(other)
