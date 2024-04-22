"""Practice writing a recursive function."""

__author__ = "730384323"


def f(n: int, k: int) -> int:
    """Recursive funtion."""
    if n == 0:  # base case
        return 0
    if n == 1:
        return k
    else:  # recursive rule
        return f(n - 1, k) + k