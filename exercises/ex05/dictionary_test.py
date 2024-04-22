"""Testing Dictionary Functions."""

__author__ = "730384323"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use_case_1() -> None:
    """Tests if invert function will reverse the keys and values of a given dictionary."""
    x: dict[str, str] = {"one": "two", "three": "four"}
    ret_value: dict[str, str] = invert(x)
    assert ret_value == {"two": "one", "four": "three"}


def test_invert_use_case_2() -> None:
    """Tests if invert function does not mutate the input dictionary."""
    x: dict[str, str] = {"one": "two", "three": "four"}
    invert(x)
    assert x == {"one": "two", "three": "four"}


def test_invert_edge_case() -> None:
    """Tests invert function when inp_dict is empty."""
    x: dict[str, str] = {}
    ret_value: dict[str, str] = invert(x)
    assert ret_value == {}


def test_favorite_color_use_case_1() -> None:
    """Tests if favorite_color will return a string of the most frequently mentioned color in a dictionary."""
    a: dict[str, str] = {"Reese": "pink", "Jada": "blue", "Sach": "pink"}  
    ret_value: str = favorite_color(a)
    assert ret_value == "pink"


def test_favorite_color_use_case_2() -> None:
    """Tests if there is a tie for most popular color, favorite_color will return the color that appeared in the dictionary first."""
    a: dict[str, str] = {"Reese": "pink", "Jada": "blue", "Sach": "pink", "Andrew": "blue"}  
    ret_value: str = favorite_color(a)
    assert ret_value == "pink"


def test_favorite_color_edge_case() -> None:
    """Tests favorite_color when inp_dict is empty."""
    a: dict[str, str] = {}
    ret_value: str = favorite_color(a)
    assert ret_value == ""


def test_count_use_case_1() -> None:
    """Tests if count produces a dictionary from an input list in which the values equal the # of times that value appeared in the list."""
    b: list[str] = ["apple", "apple", "orange", "banana"]
    ret_value: dict[str, int] = count(b)
    assert ret_value == {"apple": 2, "orange": 1, "banana": 1}


def test_count_use_case_2() -> None:
    """Tests if count function returns a dictionary of strings and integers."""
    b: list[str] = ["apple", "apple", "orange", "banana"]
    ret_value: dict = count(b)
    assert type(ret_value) is dict


def test_count_edge_case() -> None:
    """Tests count function if inp_list is empty."""
    b: list[str] = []
    ret_value: dict = count(b)
    assert ret_value == {}


def test_alphabetizer_use_case_1() -> None:
    """Tests if alphabetizer function produces a dictionary where each key is a unique letter and each value is a list of words that begin with that letter in the input list."""
    z: list[str] = ["cat", "apple", "boy", "angry", "car", "blue"]
    ret_value: dict = alphabetizer(z)
    assert ret_value == {"c": ["cat", "car"], "a": ["apple", "angry"], "b": ["boy", "blue"]}


def test_alphabetizer_use_case_2() -> None:
    """Tests if alphabetizer function returns a dictionary of strings and lists of strings."""
    z: list[str] = ["cat", "apple", "boy", "angry", "car", "blue"]
    ret_value: dict = alphabetizer(z)
    assert type(ret_value) is dict


def test_alphabetizer_edge_case() -> None:
    """Tests if alphabetizer works correctly when the words in the input list begin with both upper and lowercase letters."""
    z: list[str] = ["Cat", "apple", "Boy", "angry", "car", "blue"]
    ret_value: dict = alphabetizer(z)
    assert ret_value == {"c": ["Cat", "car"], "a": ["apple", "angry"], "b": ["Boy", "blue"]}


def test_update_attendance_use_case_1() -> None:
    """Tests if update_attendance will update a given dictionary."""
    log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(log, "Tuesday", "Reese")
    assert log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Reese"]}


def test_update_attendance_use_case_2() -> None:
    """Tests if update_attendance mutates the input dictionary."""
    log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(log, "Tuesday", "Reese")
    assert log != {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Reese"]}


def test_update_attendance_edge_case() -> None:
    """Tests update_attendance when input dictionary is empty."""
    log: dict = {}
    update_attendance(log, "Tuesday", "Reese")
    assert log == {"Tuesday": ["Reese"]}