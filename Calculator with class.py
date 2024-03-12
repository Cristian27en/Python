#calculator with int numbers

#declare variables and ask for two numbers
num1 = input('Enter a number')
num2 = input('Enter another number')

#create class and operations
class Calculator:
    def sum(self, num1, num2):
        return int(num1)+int(num2)

    def rest(self, num1, num2):
        return int(num1)-int(num2)

    def multi(self, num1, num2):
        return int(num1)*int(num2)

    def div(self, num1, num2):
        if num2==0:
            return 'error'
        return int(num1)/int(num2)

#create the instance
calc = Calculator()

#print the results
print('Sum: ', calc.sum(num1,num2), type(calc.sum(num1,num2)))
print('Rest: ', calc.rest(num1,num2), type(calc.rest(num1,num2)))
print('Multi: ', calc.multi(num1,num2), type(calc.multi(num1,num2)))
print('Division', calc.div(num1,num2), type(calc.div(num1,num2)))

#calculator with float numbers

#declare variables and ask for two numbers
num1 = input('Enter a number with decimals')
num2 = input('Enter another number with decimals')

#create class and operations
class Calculator:
    def sum(self, num1, num2):
        return float(num1)+float(num2)

    def rest(self, num1, num2):
        return float(num1)-float(num2)

    def multi(self, num1, num2):
        return float(num1)*float(num2)

    def div(self, num1, num2):
        if num2==0:
            return 'error'
        return float(num1)/float(num2)

#create the instance
calc = Calculator()

#print the results
print('Sum: ', calc.sum(num1,num2), type(calc.sum(num1,num2)))
print('Rest: ', calc.rest(num1,num2), type(calc.rest(num1,num2)))
print('Multi: ', calc.multi(num1,num2), type(calc.multi(num1,num2)))
print('Division', calc.div(num1,num2), type(calc.div(num1,num2)))