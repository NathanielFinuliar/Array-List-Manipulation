import random as rd
from collections import deque

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("|"," "*16, " "*28, "|")
print("|"," "* 10, "ARRAY LIST MANIPULATION", " " *10,"|")
print("|"," " * 8, "coded by Nathaniel Finuliar", " " *8,"|")
print("|"," " * 16, "BSCOE 2-2", " " * 18, "|")
print("|"," "*16, " "*28, "|")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

print()
array_ = [12,15,48,49,562,41,705,25,214,25]

menu_option = ["Add an element","Insert an element","Modify an element",
               "Delete an element","Arrange in ascending order","Arrange in descending order",
               "Rotate array","Shuffle arrays","Clear array"]


def _start(main_array,menu_op):
    print("-"*20)
    print(f"Array: {main_array}")
    print("Menu:")
    for i in range(len(menu_op)):
        print(f"{i+1} -> {menu_op[i]}")
    print("-"*20)
