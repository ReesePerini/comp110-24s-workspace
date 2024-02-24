"""Summing the elements of a list using different loops."""

__author__ = "730384323"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in a list of floats."""
    idx: int = 0
    sum: float = 0.0
    while idx <= len(vals) - 1:
        sum += vals[idx]
        idx += 1
    print(sum)
    return sum


x: list[float] = [1.0, 2.0, 3.0]
w_sum(x)


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in a list of floats."""
    sum: float = 0.0
    for item in vals:
        sum += item
    print(sum)
    return sum


f_sum(x)


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in a list of floats."""
    sum: float = 0.0
    for index in range(0, len(vals)):
        sum += vals[index]
    print(sum)
    return sum


f_range_sum(x)
