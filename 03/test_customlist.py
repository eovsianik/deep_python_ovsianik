from customlist import CustomList


def test_add_custom_and_custom_samesize():
    assert CustomList([5, 1, 3]) + CustomList([1, 2, 7]) == CustomList([6, 3, 10])


def test_add_custom_and_notcustom_samesize():
    assert CustomList([5, 1, 3]) + [1, 2, 7] == CustomList([6, 3, 10])


def test_add_custom_and_notcustom_emptylist():
    assert CustomList([1, 2, 7]) + [] == CustomList([1, 2, 7])


def test_add_custom_empty_and_notcustom():
    assert CustomList() + [1, 2, 7] == CustomList([1, 2, 7])


def test_add_custom_and_custom_empty():
    assert CustomList([1, 2, 7]) + CustomList() == CustomList([1, 2, 7])


def test_add_custom_empty_and_custom():
    assert CustomList() + CustomList([1, 2, 7]) == CustomList([1, 2, 7])


def test_add_custom_and_notcustom_bothempty():
    assert CustomList() + [] == CustomList()


def test_add_custom_and_custom_bothempty():
    assert CustomList() + CustomList() == CustomList()


def test_add_custom_and_custom_firstbigger():
    assert CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]) == CustomList([6, 3, 10, 7])


def test_add_custom_and_notcustom_firstbigger():
    assert CustomList([5, 1, 3, 7]) + [1, 2, 7] == CustomList([6, 3, 10, 7])


def test_add_custom_and_custom_secondbigger():
    assert CustomList([1, 2, 7]) + CustomList([10, 1, 3, 7]) == CustomList(
        [11, 3, 10, 7]
    )


def test_add_notcustom_and_custom_secondbigger():
    assert CustomList([1, 2, 7]) + [10, 1, 3, 7] == CustomList([11, 3, 10, 7])


def test_radd_notcustom_and_custom_samesize():
    assert [1, 2, 7] + CustomList([5, 1, 3]) == CustomList([6, 3, 10])


def test_radd_notcustom_emptylist_and_custom():
    assert [] + CustomList([1, 2, 7]) == CustomList([1, 2, 7])


def test_radd_notcustom_and_custom_empty():
    assert [1, 2, 7] + CustomList() == CustomList([1, 2, 7])


def test_radd_notcustom_and_custom_bothempty():
    assert [] + CustomList() == CustomList()


def test_radd_notcustom_and_custom_firstbigger():
    assert [5, 1, 3, 7] + CustomList([1, 2, 7]) == CustomList([6, 3, 10, 7])


def test_radd_custom_and_notcustom_secondbigger():
    assert [1, 2, 7] + CustomList([10, 1, 3, 7]) == CustomList([11, 3, 10, 7])


def test_sub_custom_and_custom_samesize():
    assert CustomList([5, 1, 3]) - CustomList([1, 2, 7]) == CustomList([4, -1, -4])


def test_sub_custom_and_notcustom_samesize():
    assert CustomList([5, 1, 3]) - [1, 2, 7] == CustomList([4, -1, -4])


def test_sub_custom_and_notcustom_emptylist():
    assert CustomList([1, 2, 7]) - [] == CustomList([1, 2, 7])


def test_sub_custom_empty_and_notcustom():
    assert CustomList() - [1, 2, 7] == CustomList([-1, -2, -7])


def test_sub_custom_and_custom_empty():
    assert CustomList([1, 2, 7]) - CustomList() == CustomList([1, 2, 7])


def test_sub_custom_empty_and_custom():
    assert CustomList() - CustomList([1, 2, 7]) == CustomList([-1, -2, -7])


def test_sub_custom_and_notcustom_bothempty():
    assert CustomList() - [] == CustomList()


def test_sub_custom_and_custom_bothempty():
    assert CustomList() - CustomList() == CustomList()


def test_sub_custom_and_custom_firstbigger():
    assert CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]) == CustomList(
        [4, -1, -4, 7]
    )


def test_sub_custom_and_notcustom_firstbigger():
    assert CustomList([5, 1, 3, 7]) - [1, 2, 7] == CustomList([4, -1, -4, 7])


def test_sub_custom_and_custom_secondbigger():
    assert CustomList([1, 2, 7]) - CustomList([10, 1, 3, 7]) == CustomList(
        [-9, 1, 4, -7]
    )


def test_sub_notcustom_and_custom_secondbigger():
    assert CustomList([1, 2, 7]) - [10, 1, 3, 7] == CustomList([-9, 1, 4, -7])


def test_rsub_notcustom_and_custom_samesize():
    assert [1, 2, 7] - CustomList([5, 1, 3]) == CustomList([-4, 1, 4])


def test_rsub_notcustom_emptylist_and_custom():
    assert [] - CustomList([1, 2, 7]) == CustomList([-1, -2, -7])


def test_rsub_notcustom_and_custom_empty():
    assert [1, 2, 7] - CustomList() == CustomList([1, 2, 7])


def test_rsub_notcustom_and_custom_bothempty():
    assert [] - CustomList() == CustomList()


def test_rsub_notcustom_and_custom_firstbigger():
    assert [5, 1, 3, 7] - CustomList([1, 2, 7]) == CustomList([4, -1, -4, 7])


def test_rsub_custom_and_notcustom_secondbigger():
    assert [1, 2, 7] - CustomList([10, 1, 3, 7]) == CustomList([-9, 1, 4, -7])


def test_str():
    newlist = CustomList([1, 2])
    newlist = newlist.__str__()
    new_str = newlist.split(":")
    custom, sum_customlist = new_str[0], new_str[1]
    assert custom == "[1, 2]" and sum_customlist == "3"


def test_print(capsys):
    newlist = CustomList([1, 2])
    print(newlist)
    captured = capsys.readouterr()
    new_print = captured.out
    new_print = new_print.split(":")
    custom, sum_customlist = new_print[0], new_print[1]
    assert custom == "[1, 2]" and sum_customlist == "3\n"


def test_samesize_less_than():
    assert CustomList([10, 1, 3, 7]) < CustomList([100, 1, 3, 7])


def test_firstlonger_less_than():
    assert CustomList([10, 1, 3, 7, 3, 0]) < CustomList([100, 1, 3, 7])


def test_lastlonger_less_than():
    assert CustomList([10, 1, 3, 7, 3, 0]) < CustomList([100, 1, 3, 7, 1, 2, 3, 1, 5])


def test_empty_less_than():
    assert CustomList() < CustomList([100, 1, 3, 7, 1, 2, 3, 1, 5])


def test_samesize_less_eq():
    assert CustomList([10, 1, 3, 7]) <= CustomList([100, 1, 3, 7])


def test_firstlonger_less_eq():
    assert CustomList([10, 1, 3, 7, 3, 0]) <= CustomList([100, 1, 3, 7])


def test_lastlonger_less_eq():
    assert CustomList([10, 1, 3, 7, 3, 0]) <= CustomList([100, 1, 3, 7, 1, 2, 3, 1, 5])


def test_samesize_less_alleq():
    assert CustomList([10, 1, 3, 7]) <= CustomList([1, 10, 7, 3])


def test_firstlonger_less_alleq():
    assert CustomList([10, 1, 3, 7, 3, 0]) <= CustomList([20, 4])


def test_lastlonger_less_alleq():
    assert CustomList([10, 1, 3, 7, 3]) <= CustomList([5, 1, 3, 7, 1, 2, 3, 1, 1])


def test_samesize_more_than():
    assert CustomList([100, 1, 3, 7]) > CustomList([10, 1, 3, 7])


def test_firstlonger_more_than():
    assert CustomList([100, 1, 3, 7, 2050]) > CustomList([10, 1, 3])


def test_lastlonger_more_than():
    assert CustomList([100, 1]) > CustomList([10, 1, 3, 7, 3, 0])


def test_empty_more_than():
    assert CustomList([100, 1]) > CustomList()


def test_samesize_more_eq():
    assert CustomList([1000, 1, 3, 7]) >= CustomList([10, 1, 3, 7])


def test_firstlonger_more_eq():
    assert CustomList([10, 1, 3, 7, 3, 1000]) >= CustomList([100, 1, 3, 7])


def test_lastlonger_more_eq():
    assert CustomList([1000, 1]) >= CustomList([100, 1, 3, 7, 1, 2, 3, 1, 5])


def test_samesize_more_alleq():
    assert CustomList([10, 1, 3, 7]) >= CustomList([10, 1, 3, 7])


def test_firstlonger_more_alleq():
    assert CustomList([1, 3, 5, 2, 1000]) >= CustomList([1000, 1, 3, 7])


def test_lastlonger_more_alleq():
    assert CustomList([1000, 5]) >= CustomList([1000, 2, 3])


def test_samesize_alleq():
    assert CustomList([11, 3, 2, 5]) == CustomList([10, 1, 3, 7])


def test_firstlonger_alleq():
    assert CustomList([2, 3, 4, 2, 500, 500]) == CustomList([1, 3, 5, 2, 1000])


def test_lastlonger_alleq():
    assert CustomList([1000, 5]) == CustomList([525, 475, 2, 3])


def test_samesize_noteq():
    assert CustomList([11, 3, 2, 500]) != CustomList([10, 1, 3, 7])


def test_firstlonger_noteq():
    assert CustomList([2, 3, 4, 2, 500, 700]) != CustomList([1, 3, 5, 2, 1000])


def test_lastlonger_noteq():
    assert CustomList([1000, 500]) != CustomList([525, 475, 2, 3])


def test_empty_noteq():
    assert CustomList([1000, 500]) != CustomList()


def test_inoutput_notchanged_add():
    first = CustomList([])
    second = CustomList([1, 2, 3])
    third = CustomList([-1, 2, 3])
    forth = [2, 3]
    result = first + second + third + forth
    assert (
        first.__str__() == "[]:0"
        and second.__str__() == "[1, 2, 3]:6"
        and third.__str__() == "[-1, 2, 3]:4"
        and forth == [2, 3]
        and result.__str__() == "[2, 7, 6]:15"
    )
    assert (
        isinstance(first, CustomList)
        and isinstance(second, CustomList)
        and isinstance(third, CustomList)
        and isinstance(forth, list)
    )
    assert isinstance(result, CustomList)
    assert (
        forth == [2, 3]
        and list(second) == [1, 2, 3]
        and list(third) == [-1, 2, 3]
        and list(first) == []
        and list(result) == [2, 7, 6]
    )


def test_inoutput_notchanged_radd():
    first = [2, 3]
    second = CustomList([1, 2, 3])
    third = CustomList([-1, 2, 3])
    forth = CustomList([])
    result = first + second + third + forth
    assert (
        first == [2, 3]
        and second.__str__() == "[1, 2, 3]:6"
        and third.__str__() == "[-1, 2, 3]:4"
        and forth.__str__() == "[]:0"
        and result.__str__() == "[2, 7, 6]:15"
    )
    assert (
        isinstance(first, list)
        and isinstance(second, CustomList)
        and isinstance(third, CustomList)
        and isinstance(forth, CustomList)
    )
    assert isinstance(result, CustomList)
    assert (
        first == [2, 3]
        and list(second) == [1, 2, 3]
        and list(third) == [-1, 2, 3]
        and list(forth) == []
        and list(result) == [2, 7, 6]
    )


def test_inoutput_notchanged_sub():
    first = CustomList([])
    second = CustomList([1, 2, 3])
    third = CustomList([-1, 2, 3])
    forth = [2, 3]
    result = first - second - third - forth
    assert (
        first.__str__() == "[]:0"
        and second.__str__() == "[1, 2, 3]:6"
        and third.__str__() == "[-1, 2, 3]:4"
        and forth == [2, 3]
        and result.__str__() == "[-2, -7, -6]:-15"
    )
    assert (
        isinstance(first, CustomList)
        and isinstance(second, CustomList)
        and isinstance(third, CustomList)
        and isinstance(forth, list)
    )
    assert isinstance(result, CustomList)
    assert (
        forth == [2, 3]
        and list(second) == [1, 2, 3]
        and list(third) == [-1, 2, 3]
        and list(first) == []
        and list(result) == [-2, -7, -6]
    )


def test_inoutput_notchanged_rsub():
    first = [2, 3]
    second = CustomList([1, 2, 3])
    third = CustomList([-1, 2, 3])
    forth = CustomList([])
    result = first - second - third - forth
    assert (
        first == [2, 3]
        and second.__str__() == "[1, 2, 3]:6"
        and third.__str__() == "[-1, 2, 3]:4"
        and forth.__str__() == "[]:0"
        and result.__str__() == "[2, -1, -6]:-5"
    )
    assert (
        isinstance(first, list)
        and isinstance(second, CustomList)
        and isinstance(third, CustomList)
        and isinstance(forth, CustomList)
    )
    assert isinstance(result, CustomList)
    assert (
        first == [2, 3]
        and list(second) == [1, 2, 3]
        and list(third) == [-1, 2, 3]
        and list(forth) == []
        and list(result) == [2, -1, -6]
    )
