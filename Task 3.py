m = float(input('Enter the number to convert: '))
task = int(input('Enter the number of the operation to be performed on the numbers (1 - miles; 2 - inches; 3 - yards): '))

if task == 1:
    # miles
    print('mi:', round(m*0.0006213712, 5))
elif task == 2:
    # inches
    print('in:', round(m*39.370079, 5))
else:
    # yards
    print('yd:', round(m*1.093613, 5))