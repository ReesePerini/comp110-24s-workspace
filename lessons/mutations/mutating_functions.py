"""Functions that either mutate a list or don't."""

def remove_first(input_list: list[str]) -> None:
    """"Remove first element of input_list. Mutating!"""
    input_list.pop(0)


def get_first(input_list: list[str]) -> str:
    """Return first element of list without mutating."""
    return input_list[0]

def get_and_remove_first(input_list: list[str]) -> str:
    """Return AND remove first element of list."""
    elem: str = input_list[0]
    input_list.pop(0)
    return elem