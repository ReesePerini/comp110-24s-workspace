"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730384323"

player1_input: str = input("Pick a secret boat location between 1 and 4: ")
player1_number: int = int(player1_input)

if player1_number < 1:
    print("Error! " + player1_input + " too low!")
    exit()
if player1_number > 4:
    print("Error! " + player1_input + " too high!")
    exit()

player2_input: str = input("Guess a number between 1 and 4: ")
player2_number: int = int(player2_input)

if player2_number < 1:
    print("Error! " + player2_input + " too low!")
    exit()
if player2_number > 4:
    print("Error! " + player2_input + " too high!")
    exit()

result_str: str = ""
result_box: str = ""
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if player2_number == player1_number:
    print("Correct! You hit the ship.")
    result_box = RED_BOX
else:
    print("Incorrect! You missed the ship.")
    result_box = WHITE_BOX

if player2_number == 1:
    result_str += result_box
else:
    result_str += BLUE_BOX

if player2_number == 2:
    result_str += result_box
else:
    result_str += BLUE_BOX

if player2_number == 3:
    result_str += result_box
else:
    result_str += BLUE_BOX

if player2_number == 4:
    result_str += result_box
else:
    result_str += BLUE_BOX

print(result_str)