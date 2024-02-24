"""Mutating functions."""

__author__ = "730384323"


def manual_append(my_list: list[int], number: int) -> None:
    """The function will append the int parameter to the end of the list parameter."""
    my_list.append(number)
    print(my_list)


x: list[int] = [1, 2, 3]
manual_append(x, 4)


def double(my_list: list[int]) -> None:
    """The function will multiply every element in my_list by 2."""
    idx: int = 0
    while idx <= len(my_list) - 1:
        my_list[idx] = my_list[idx] * 2
        idx += 1
    print(my_list)


y: list[int] = [2, 4, 6]
double(y)
