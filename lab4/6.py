age = input('Введіть Ваш вік: ')
number = 0
while True:
  number += 1
  if age == 'exit': break
  elif int(age) < 3:
    print(str(number) + ' Квиток безкоштовний')
  elif int(age) >= 3 and int(age) <= 12:
    print(str(number) + ' Квиток коштує 50 грн.')
  else:
    print(str(number) + ' Квиток коштує 80 грн.')
  age = input('Введіть Ваш вік: ')
