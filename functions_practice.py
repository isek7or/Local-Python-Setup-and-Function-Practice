# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print("hello")

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(arg_1, arg_2, arg_3):
    return [arg_1, arg_2, arg_3]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty!")
    for food_index in range(len(my_lunch)):
        if food_index == 0:
            print(f"First I eat {my_lunch[food_index]}")
        elif food_index < len(my_lunch):
            print(f"Then I eat {my_lunch[food_index]}")
        else:
            print("My lunchbox is empty")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])
