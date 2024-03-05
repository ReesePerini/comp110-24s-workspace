"""Splitting a dictionary into two lists."""

__author__ = "730384323"


def get_keys(my_dict: dict[str, int]) -> list[str]:
    """Produces a list of all keys in the input dictionary."""
    my_list: list[str] = []
    for key in my_dict:
        my_list.append(key)
    if my_dict == {}:
        empty_list: list[str] = []
        print(empty_list)
        return empty_list
    print(my_list)
    return my_list


x: dict[str, int] = {"Hello": 1, "World": 2}
get_keys(x)

y: dict[str, int] = {}
get_keys(y)


def get_values(my_dict: dict[str, int]) -> list[int]:
    """Produces a list of all values in the input dictionary."""
    my_list: list[int] = []
    for key in my_dict:
        my_list.append(my_dict[key])
    if my_dict == {}:
        empty_list: list[int] = []
        print(empty_list)
        return empty_list
    print(my_list)
    return my_list


get_values(x)
get_values(y)