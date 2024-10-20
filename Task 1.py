a, b, c = map(int, input('Enter three numbers separated by commas: ').split(','))
task = int(input('Enter the number of the operation to be performed on the numbers (1 - sum; 2 - product): '))

if task == 1:
    # Sum
    print('Sum of numbers:', a+b+c)
elif task == 2:
    # Product
    print('Product of numbers:', a*b*c)