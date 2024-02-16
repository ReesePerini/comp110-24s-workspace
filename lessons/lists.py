"""Demonstrate basic list syntax."""

#initialize an empty list
grocery_list: list[str] = list() #list constructor
grocery_list: list[str] = [] #literal

print(grocery_list)

#add item to list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending:")
print(grocery_list)

#create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]

print("Populated list:")
print(grocery_list2)

grocery_list2.append("eggs")

print(grocery_list2[0])

#modifying by index
print("before change:")
print(grocery_list)

grocery_list[1] = "almond milk"

print("after change")
print(grocery_list)

#measuring length
print("length of list:")
print(len(grocery_list))

#removing item from list
grocery_list.pop(1)
print("after removing an item:")
print(grocery_list)

#Function name: display
#Parameter: list[str]
#Return nothing
#Print out the list

def display(my_list: list[str]) -> None:
    """given my_list, print my_list."""
    print(my_list)

x = display(grocery_list2)
print(x)

#create a list
#Name: create
#Parameters: str and str
#RV: list[str]
#put both parameters into list

def create(word1: str, word2: str) -> list[str]:
    """put both parameters into a list"""
    my_list: list[str] = [word1, word2]
    return my_list

x = create("head", "shoulders")
print(x)
