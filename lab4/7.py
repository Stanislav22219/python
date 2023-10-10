import random

r = random.random() * 100 + 1
r = int(r)
print(r)
n = input('Вгадайте число від 1 до 100: ')
while True:
    if str(n) == 'exit':
            break
    elif n.isdigit() == True:
        if str(r) == n:
            print('Ви вгадали число: ' + str(r))
            break
        elif int(str(r)) > int(n):
            print('Число більше введеного')
            n = (input('Вгадайте число від 1 до 100: '))
        elif r < int(n):
            print('Число менше введеного')
            n = input('Вгадайте число від 1 до 100: ')
    elif n.isdigit() == False:
        print('Введено не число')
        n = input('Вгадайте число від 1 до 100: ')

