# Define some functions
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def double(x):
    return x * 2

# Create a list of functions
functions_list = [square, cube, double]

# Use the functions from the list
for func in functions_list:
    result = func(5)  # Call each function with argument 5
    print("Result:", result)
