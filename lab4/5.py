word = input()
i = 0
consonants = 'бвгґджзклмнпрстфхцчшщБВГҐДЖЗКЛМНПРСТФХЦЧШЩ'
result = ''
while i < len(word):
    if word[i] in consonants:
        result += word[i]
    i+=1
print(result)
