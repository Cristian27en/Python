#Calculator with int numbers

num1 = input('Enter a number')
num2 = input('Enter another number')

#sum
def sum(num1,num2):
    result = int(num1) + int(num2)
    print('Sum: ', result, type(result))

sum(num1,num2)

#rest
def rest(num1, num2):
    result = int(num1) - int(num2)
    print('Rest: ', result, type(result))

rest(num1,num2)

#multiplpier
def multi(num1, num2):
    result = int(num1) * int(num2)
    print('Multiplier: ', result, type(result))

multi(num1,num2)

#division
def div(num1, num2):
    result = int(num1) / int(num2)
    print('Multiplier: ', result, type(result))

div(num1,num2)

#Calculator with float numbers

num1 = input('Enter a number with decimals')
num2 = input('Enter another number with decimals')

#sum
def sum(num1,num2):
    result = float(num1) + float(num2)
    print('Sum: ', result, type(result))

sum(num1,num2)

#rest
def rest(num1, num2):
    result = float(num1) - float(num2)
    print('Rest: ', result, type(result))

rest(num1,num2)

#multiplpier
def multi(num1, num2):
    result = float(num1) * float(num2)
    print('Multiplier: ', result, type(result))

multi(num1,num2)

#division
def div(num1, num2):
    result = float(num1) / float(num2)
    print('Multiplier: ', result, type(result))

div(num1,num2)

