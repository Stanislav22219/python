a, b, c = input('Введіть три числа: ').split()
if (int(a) > int(b)) and (int(a) > int(c)):
    print('Перше число найбільше')
elif (int(b) > int(a)) and (int(b) > int(c)):
    print('Друге число найбільше')
elif (int(c) > int(a)) and (int(c) > int(b)):
    print('Третє число найбільше')
