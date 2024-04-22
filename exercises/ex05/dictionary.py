"""Practice with Dictionary Functions."""

__author__ = "730384323"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    new_dict: dict[str, str] = {}
    for key in inp_dict:
        if inp_dict[key] in new_dict:
            raise KeyError(f"The key {key} already exists in the dictionary.")
        else:
            new_dict[inp_dict[key]] = key

    print(new_dict)
    return new_dict
    

x: dict[str, str] = {"one": "two", "three": "four"}
invert(x)


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Returns a string of most frequently mentioned color."""
    if inp_dict == {}:
        return ""
    fave_color: str = ""
    color_count: dict[str, int] = {}
    for name in inp_dict:
        if inp_dict[name] in color_count:
            color_count[inp_dict[name]] += 1
        else: 
            color_count[inp_dict[name]] = 1
    max_count: int = 0
    for key in color_count:
        if color_count[key] > max_count:
            max_count = color_count[key]
            fave_color = key
    print(fave_color)
    return fave_color


a: dict[str, str] = {"Reese": "pink", "Jada": "blue", "Sach": "pink"}  
favorite_color(a)

t: dict[str, str] = {"Reese": "pink", "Jada": "blue", "Sach": "green"}
favorite_color(t)


def count(inp_list: list[str]) -> dict[str, int]:
    """Produces a dictionary from a list in which each value equals the # of times that value appeared in the input list."""
    if inp_list == []:
        return {}
    count_dict: dict[str, int] = {}
    for item in inp_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    print(count_dict)
    return count_dict
          

b: list[str] = ["apple", "apple", "orange", "banana"]
count(b)


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Produces a dictionary where each key is a unique letter and each value is a list of words that begin with that letter in the input list."""
    alpha_dict: dict[str, list[str]] = {}
    for item in inp_list:
        if item[0] in alpha_dict:
            alpha_dict[item[0].lower()].append(item)
        else:
            alpha_dict[item[0].lower()] = [item]
    print(alpha_dict)
    return alpha_dict


z: list[str] = ["Cat", "apple", "boy", "angry", "car", "blue"]
alphabetizer(z)


def update_attendance(inp_dict: dict[str, list[str]], day: str, name: str) -> None:
    """Given a dictionary, this function will update the dictionary."""
    if day in inp_dict:
        inp_dict[day].append(name)
    else:
        inp_dict[day] = [name]
    print(inp_dict)


log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(log, "Tuesday", "Reese")