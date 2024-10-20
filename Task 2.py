a, b, c = map(int, input('Enter three numbers separated by commas: ').split(','))
task = int(input('Enter the number of the operation to be performed on the numbers (1 - maximum of three; 2 - minimum of three; 3 - arithmetic mean): '))

if task == 1:
    # maximum of three
    if a > b and a > c:
        print(a, 'the largest of the three')
    elif b > a and b > c:
        print(b, 'the largest of the three')
    else:
        print(c, 'the largest of the three')
elif task == 2:
    # minimum of three
    if a < b and a < c:
        print(a, 'is the least of the three')
    elif b < a and b < c:
        print(b, 'is the least of the three')
    else:
        print(c, 'is the least of the three')
elif task == 3:
    # arithmetic mean
    print(int((a+b+c)/3))