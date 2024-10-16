import sys
class Calculator:
    def add(self, a, b):
        return a + b
    def subract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return ('Invalid Divisor')
def main():
    calculator = Calculator()
    print('Calculator can perform these operations -')
    print('1. Add')
    print('2. Subract')
    print('3. Multiply')
    print('4. Divide')

    select = int(input('Select the operations from 1, 2, 3, 4: '))
    for i in range(5):
        if(select == 1 or select == 2 or select == 3 or select == 4):
            break          
        else:
            if i == 4:
                print('Maximum limit reached, please try running it again.')
                sys.exit()
            print('Invalid input, please enter again:')
            select = int(input('Select the operation from 1, 2, 3, 4: '))


    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    if select == 1:
        print(num1, '+', num2, '=', calculator.add(num1, num2))
    elif select == 2:
        print(num1, '-', num2, '=', calculator.subract(num1, num2))
    elif select == 3:
        print(num1, 'x', num2, '=', calculator.multiply(num1, num2))
    else:
        print(num1, '/', num2, '=', calculator.divide(num1, num2))

main()

    



