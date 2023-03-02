import random as rd 
from collections import deque

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("|"," "*16, " "*28, "|")
print("|"," "* 10, "ARRAY LIST MANIPULATION", " " *10,"|")
print("|"," " * 8, "coded by Nathaniel Finuliar", " " *8,"|")
print("|"," " * 16, "BSCOE 2-2", " " * 18, "|")
print("|"," "*16, " "*28, "|")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

array_ = [12,15,48,49,562,41,705,25,214,25]

menu_option = ["Add an element","Insert an element","Modify an element",
               "Delete an element","Arrange in ascending order","Arrange in descending order",
               "Rotate array","Shuffle arrays","Clear array"]


def _start(main_array,menu_op):
    print(" "*20)
    print(f"Array: {main_array}")
    print()
    print("Menu:")
    for i in range(len(menu_op)):
        print(f"{i+1} -> {menu_op[i]}")
    print(" "*20)
    while True:
        try:
            option_select = int(input("What you want to do? (1-9) : "))
            if option_select in range(1,10):
                return option_select
            else:
                print("Range Exceeded!")
        except:
            print("Invalid input try again!")

def add_element(main_array):
    while True:
        try:
            s = int(input("Enter value you want to add: "))
            main_array.append(s)
            print(f"{s} has been added to array")
            return
        except:
            print("Invalid input try again!")


def insert_element(main_array):
    # If the index is exceed length of the array it will just throw the item to the end of the array
    # This method recieves input from user with is seperated by space ex. "1 2 3 4 5 6"
    while True:
        try:
            # Create two variables to hold that seperated value, in this case
            # We need two variables because we need two value (index,value)
            index,value = [int(i) for i in input("Enter the index follow up by the value you want to add: ").split()]
            main_array.insert(index,value)
            print(f"{value} has been added to array at the index of {index}")
            return
        except:
            print("Invalid input try again!")

def modify_element(main_array):
    while True:
        try:
            index_m,value_m = [int(i) for i in input("Enter the index follow up by the value you want to modify: ").split()]
            temp_value = main_array[index_m]
            main_array[index_m] = value_m
            print(f"{temp_value} at the index {index_m} has been modified to {value_m}")
            return
        except:
            print("Invalid input try again!")    

def remove_element(main_array):
    while True:
        try:
            option_del = int(input("Do you want to delete by value or index (value : 1 , index : 2) : "))
            # Here we seperated to two cases
            if option_del == 1:
                item = int(input("What do you want to delete ? : ")) 
                array_.remove(item)  # remove will delete the element by value
            elif option_del == 2:
                index_del = int(input("Which index do you want to delete ? : "))
                del main_array[index_del] # remove will delete the element by index
            return
        except:
            print("Invalid input try again!")

def sort_array(main_array):
    main_array = main_array.sort()
    print("Array has been sorted in ascending order")

def reverse_array(main_array):
    main_array = main_array.sort(reverse=True)
    print("Array has been sorted in descending order")

def rotate_element(main_array):
    global array_ 
    array_= deque(array_)  # Convert array to deque object make it usable for deque's methods
    valid_step= False 
    valid_side= False
    while not valid_step:
        try:
            step = int(input("How many steps do you want to rotate? : "))
            if step > len(array_):
                print("Step is more than array's length")
            elif step <= 0:
                print("Step must be greater than zero")
            else:
                valid_step = True
        except:
            print("Invalid input try again!")
        
    while not valid_side:
        side = input("Which way you want to rotate? (L for Left / R for Right) : ")
        if side.upper() == 'L' or side.upper() == 'R':
            if side.upper() == 'L':
                array_.rotate(-abs(step))  # Set the -abs here for left rotate becuase left rotate need negative integer
            elif side.upper() == 'R':
                array_.rotate(abs(step)) # Same as above but right need positive integer
            valid_side = True #If this scope run we set this boolean to True so, the loop won't run again
        else:
            print("Invalid input try again!")
    # Convert array_ to list due of converting array_ to deque object
    array_ = list(array_)

def shuffle_array(main_array):
    x = rd.shuffle(main_array)
    main_array = x 
    print("Array has been shuffled")

def clear_array(main_array):
    if len(main_array) > 0:
        main_array = main_array.clear()
        print("All elements in array have been cleared")
    else:
        print("Array is already emptied")

# Created dictionary that carries function in it
# I use integer number for a key and functions's names as value
menu_function = {1:add_element,2:insert_element,3:modify_element,
                 4:remove_element,5:sort_array,6:reverse_array, 
                 7:rotate_element, 8:shuffle_array,9:clear_array}

# In order to access function from dictionary
def function_runner():
    menu_function[_start(array_,menu_option)](array_) 
    print(f"This is the new array : {array_}")

exit_ = False
start = True
while not exit_:
    if start:
        function_runner()
        start = False
    pull_request = input("Do you want to do anything else (y/n)? : ")
    if pull_request.lower() in ['y','n']:
        if pull_request.lower() == 'n':
            print("Exiting...")
            print("")
            print("-%-"*3, "THANK YOU FOR USING THIS PROGRAM","-%-"*3)
            print("")
            exit_ = True
        else:
            function_runner()
    else:
        print("Invalid input try again!")
