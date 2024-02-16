"""Functional Battleship."""

__author__ = "730384323"

import random

def input_guess(grid_size: int, user_input: str) -> int:
    """The function will prompt for and return user's row or column guess."""
    assert user_input == "row" or user_input == "column"
    if user_input == "row":
        row_input: int = int(input("Guess a row: "))
        while row_input > grid_size or row_input < 1:
            error1_input: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            row_input = error1_input
        return row_input
    elif user_input == "column":
        column_input: int = int(input("Guess a column: "))
        while column_input > grid_size or column_input < 1:
            error2_input: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            column_input = error2_input
        return column_input

def print_grid(grid_size: int, row_guess: int, column_guess: int, answer: bool) -> None:
    """The function will print a grid of boxes to represent the game board."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box: str = ""
    row_count: int = 1
    if answer == True:
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX
    while row_count <= grid_size:
        result_str: str = ""
        column_count: int = 1
        if row_guess == row_count:
            while column_count <= grid_size:
                if column_guess == column_count:
                    result_str += result_box
                else:
                    result_str += BLUE_BOX
                column_count += 1
        else:
            while column_count <= grid_size:
                result_str += BLUE_BOX
                column_count += 1  
        print(result_str)
        row_count += 1

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Given secret boat location and user guess, the function will return if the user was correct or not."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Pull all functions together to create game."""
    turn_number: int = 1
    end: bool = False
    while turn_number <= 5 and end == False:
        print(f"=== Turn {turn_number}/5 ===")
        row_input: int = input_guess(grid_size, "row")
        column_input: int = input_guess(grid_size, "column")
        correct_bool: bool = correct_guess(secret_row, secret_column, row_input, column_input)
        print_grid(grid_size, row_input, column_input, correct_bool)
        if correct_bool == True:
            print(f"Hit! You won in {turn_number}/5 turns!")
            turn_number = 6
            end = True
        elif turn_number < 5:
            print("Miss!")
            turn_number += 1
        else:
            print("X/5 - Better luck next time!")
            turn_number = 6
            end: True

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))


