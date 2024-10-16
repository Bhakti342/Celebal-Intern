rows = int(input('Enter number of rows: '))

def upper_triangle():
    for i in range(1, rows + 1):
        for j in range(i):
            print('* ', end = '')
        print()

upper_triangle()
print()

def lower_triangle():
    for i in range(rows, 0, -1):
        for j in range(i):
            print('* ', end = '')
        print()

lower_triangle()
print()


def pyramid():
    for i in range(1, rows+1):
        for j in range(rows - i):
            print(' ', end = '')
        for k in range(i):
            print('* ', end = '')
        print()

pyramid()
