"""List Utility Functions."""

__author__ = "730384323"


def all(my_list: list[int], my_number: int) -> bool:
    """Returns a bool indicating whether or not all list ints are the same as a given int."""
    condition: bool = False
    if len(my_list) == 0:
        condition = False
        print(condition)
        return condition
    for item in my_list:
        if item == my_number:
            condition = True
        else:
            condition = False
            print(condition)
            return False
    print(condition)
    return True
        

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


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns True if lists are equal, False otherwise."""
    if len(list_1) == 0 and len(list_2) == 0:
        print(True)
        return True
    if len(list_1) == 0 and len(list_2) != 0 or len(list_2) == 0 and len(list_1) != 0:
        print(False)
        return False
    if len(list_1) == len(list_2):
        idx: int = 0
        condition: bool = False
        while idx <= len(list_1) - 1:
            if list_1[idx] == list_2[idx]:
                condition = True
            else:
                condition = False
                print(condition)
                return condition
            idx += 1
        print(condition)
        return condition
    else:
        correct: bool = False
        for elem in list_1:
            for item in list_2:
                if item == elem:
                    correct = True
                else:
                    correct = False
                    print(correct)
                    return correct
        for item in list_2:
            for elem in list_1:
                if elem == item:
                    correct = True
                else:
                    correct = False
                    print(correct)
                    return correct
        print(correct)
        return correct


a: list[int] = []
b: list[int] = []
c: list[int] = [1, 0, 1]

is_equal(a, b)
is_equal(a, c)


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Mutate the first list by appending the second list to the end of it."""
    for item in list_2:
        list_1.append(item)
    print(list_1)