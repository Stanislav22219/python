text = ' Думи мої, думи мої, Лихо мені з вами! Нащо стали на папері Сумними рядами?.. Чом вас вітер не розвіяв В степу, як пилину? Чом вас лихо не приспало, Як свою дитину?... '

#1
print(text.count(' ',1))
#2
print(len(text))
#3
text = text.strip()
print(text)
#4
index = text.find('Чом')
text1 = text[index:]
print(text1)
#5
splitted_text = text1.split('?')
print(splitted_text)
#6
print(text.replace('степу', 'полі'))
#7
print(text.find('вітер'))
#8
print(text.upper())
#9
print(text.lower())
