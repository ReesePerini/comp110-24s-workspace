"""QZ 02 practice problem"""

def odd_and_even(my_list: list[int]) -> list[int]:
    """Returns even index + odd value"""
    new_list: list[int] = []
    idx: int = 0
    for elem in my_list:
        if elem % 2 == 1 and idx % 2 == 0:
            new_list.append(elem)
        idx += 1
    print(new_list)

x: list[int] = [1, 2, 3, 4, 5]

odd_and_even(x)