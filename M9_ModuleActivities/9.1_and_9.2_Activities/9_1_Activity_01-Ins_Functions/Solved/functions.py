# Basic function
# def name():
#    print("This is a basic function")
#    return

# # Use basic function
# name()

# # Functions can have more than one parameter
# def make_quesadilla(protein, topping):
#     quesadilla = f'Here is a {protein} quesadilla with {topping}'
#     print(quesadilla)
#     return

# # Supply the arguments (values) when calling the function
# make_quesadilla("beef", "guacamole")
# # @: Order is important when supplying arguments! unless it is explicitly called
# make_quesadilla("sour cream", "beef")
# make_quesadilla(topping="salsa", protein="chicken")


# # We can also specify default values for parameters
# def make_quesadilla(protein, topping="sour cream"):
#     quesadilla = f"Here is a {protein} quesadilla with {topping}"
#     print(quesadilla)


# # Make a quesadilla using the default topping
# make_quesadilla("chicken")

# # Make a quesadilla with a new topping
# make_quesadilla("beef", "guacamole")


# # Functions can return a value
def square(number):
    return number * number


# # You can save the value that is returned
# print(square(2))


# # You can also just print the return value of a function
print(square(2))
print(square(3))
