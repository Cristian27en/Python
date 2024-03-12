# define functions
def sum(x, y):
    return x + y


def rest(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return 'Division by zero is not allowed'
    else:
        return x / y

# move the functions in list
ArrayCalculator = [sum, rest, multi, div]

# assign each function reference to a variable
OpSum = ArrayCalculator[0]
OpRest = ArrayCalculator[1]
OpMulti = ArrayCalculator[2]
OpDiv = ArrayCalculator[3]

# then can easily call to the functions using the reference variables
# and assigning numbers to x and y

print(OpSum(3, 1))
print(OpRest(52, 16))
print(OpMulti(123, 3))
print(OpDiv(128, 2))

# other option
for func in ArrayCalculator:
    result = func(5, 5)
    print("Result:", result)
