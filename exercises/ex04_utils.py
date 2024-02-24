"""List Utility Functions."""

__author__ = "730384323"


def all(my_list: list[int], my_number: int) -> bool:
    """Returns a bool indicating whether or not all list ints are the same as a given int."""
    condition: bool = False
    for item in my_list:
        if item == my_number:
            condition = True
        else:
            condition = False
            print(condition)
            return False
    print(condition)
    return True
        

x: list[int] = [1, 2, 3]
y: list[int] = [1, 2, 3]

all(x, 1)
all(y, 1)


def max(my_list: list[int]) -> int:
    """Returns the largest # in a list. ValueError if list is empty."""
    if len(my_list) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max: int = my_list[idx]
    for item in my_list:
        if item > my_list[idx]:
            max = item
            idx += 1
    print(max)
    return max


max(x)
max(y)

a: list[int] = [2, 4, 6]
b: list[int] = [2, 4, 6]

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns True if lists are equal, False otherwise."""
    idx_1: int = 0
    idx_2: int = 0
    while idx_1 <= len(list_1) - 1 or idx_2 <= len(list_2) - 1:
        if list_1[idx_1] == list_2[idx_2]:
            equal: bool = True
        else:
            not_equal: bool = False
            print(not_equal)
            return not_equal
        idx_1 += 1
        idx_2 += 1
    print(equal)
    return equal


is_equal(a, b)


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Mutate the first list by appending the second list to the end of it."""
    for item in list_2:
        list_1.append(item)
    print(list_1)


extend(a, b)