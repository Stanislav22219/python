a, b = input('Введіть два числа: ').split()
if int(a) > int(b):
    print('Друге число менше першого')
elif int(a) < int(b):
    print('Перше число менше другого')
else:
    print('Числа рівні')
