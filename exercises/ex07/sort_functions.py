"""Functions that implement sorting algorithms."""

__author__ = "730384323"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    sorted_idx: int = 0
    while sorted_idx < len(x) - 1:
        unsorted_idx: int = sorted_idx + 1
        current_elem: int = x[unsorted_idx]
        while unsorted_idx > 0 and current_elem < x[unsorted_idx-1]:
            x[unsorted_idx] = x[unsorted_idx-1]
            x[unsorted_idx-1] = current_elem
            unsorted_idx -= 1
        sorted_idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx1: int = 0
    while idx1 < len(x):
        idx2: int = idx1
        min_idx: int = idx1
        while idx2 < len(x):
            if x[idx2] < x[min_idx]:
                min_idx = idx2
            idx2 += 1
        if x[min_idx] < x[idx1]:
            temp: int = x[min_idx]
            x[min_idx] = x[idx1]
            x[idx1] = temp
        idx1 += 1            
    return None