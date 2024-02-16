"""One Shot Battleship!"""

__author__ = "730384323"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_input: str = input("Guess a row: ")
row_number: int = int(row_input)

while row_number > 4 or row_number < 1:
    error1_input: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    row_number = error1_input

column_number: int = int(input("Guess a column: "))

while column_number > 4 or column_number < 1:
    error2_input: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    column_number = error2_input

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result_box: str = ""
row_count: int = 1

if row_number == secret_row and column_number == secret_column:
    result_box = RED_BOX
elif row_number == secret_row:
    result_box = WHITE_BOX
elif column_number == secret_column:
    result_box = WHITE_BOX
else:
    result_box = WHITE_BOX

while row_count <= grid_size:
    result_str: str = ""
    column_count: int = 1
    if row_number == row_count:
        while column_count <= grid_size:
            if column_number == column_count:
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

if row_number == secret_row and column_number == secret_column:
    print("Hit!")
    result_box = RED_BOX
elif row_number == secret_row:
    print("Close! Correct row, wrong column.")
    result_box = WHITE_BOX
elif column_number == secret_column:
    print("Close! Correct column, wrong row.")
    result_box = WHITE_BOX
else:
    print("Miss!")
    result_box = WHITE_BOX